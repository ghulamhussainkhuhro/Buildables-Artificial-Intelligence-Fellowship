import os
import tempfile
import fitz  # for PDFs
import docx
import streamlit as st
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import SystemMessage, HumanMessage, AIMessage
from pinecone import Pinecone, ServerlessSpec, CloudProvider, AwsRegion, Metric


load_dotenv()
groq_api = os.getenv("GROQ_API_KEY")
pinecone_api = os.getenv("PINECONE_API_KEY")

if not all([groq_api, pinecone_api]):
    st.error("Please set GROQ_API_KEY and PINECONE_API_KEY in your .env file.")
    st.stop()

pc = Pinecone(api_key=pinecone_api)

st.title("Mini RAG App — Ask Questions from Your Document")
st.write("Upload a PDF or DOCX file and start chatting with its content!")

uploaded_file = st.file_uploader("Upload a file", type=["pdf", "docx"])

def extract_text(file_path):
    text = ""
    if file_path.endswith(".pdf"):
        with fitz.open(file_path) as doc:
            for page in doc:
                text += page.get_text("text")
    elif file_path.endswith(".docx"):
        doc = docx.Document(file_path)
        for para in doc.paragraphs:
            text += para.text + "\n"
    return text.strip()

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{uploaded_file.name.split('.')[-1]}") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    st.success("File uploaded successfully!")
    text = extract_text(tmp_path)

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = splitter.split_text(text)
    st.info(f"Document split into {len(chunks)} chunks.")

    # Pinecone index setup
    index_name = "week5-rag-app"
    dimension = 384

    if index_name not in [i["name"] for i in pc.list_indexes()]:
        pc.create_index(
            name=index_name,
            metric=Metric.DOTPRODUCT,
            dimension=dimension,
            spec=ServerlessSpec(cloud=CloudProvider.AWS, region=AwsRegion.US_EAST_1)
        )

    index = pc.Index(index_name)

    # Embeddings
    embed_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # Upload vectors
    with st.spinner("Generating embeddings and uploading to Pinecone..."):
        vectors = embed_model.embed_documents(chunks)
        to_upsert = [(f"id-{i}", vectors[i], {"text": chunks[i]}) for i in range(len(chunks))]
        index.upsert(vectors=to_upsert)
    st.success("Embeddings uploaded successfully!")

    # Vector store + retriever
    vectorstore = PineconeVectorStore(index=index, embedding=embed_model, text_key="text")
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    # Chat model
    chat = ChatGroq(groq_api_key=groq_api, model_name="Llama-3.3-70B-Versatile")

    system_prompt = SystemMessage(
        content="You are a helpful assistant. Use the document context to answer questions. "
                "If the answer is not found, say 'I don't know.'"
    )
    message_history = [system_prompt]

    st.markdown("---")
    st.subheader("Chat with your document")

    query = st.text_input("Ask a question about the uploaded document:")

    if query:
        docs = retriever.get_relevant_documents(query)
        context = "\n\n".join([d.page_content for d in docs])
        user_prompt = f"Context:\n{context}\n\nQuestion:\n{query}"
        user_msg = HumanMessage(content=user_prompt)
        message_history.append(user_msg)
        response = chat(message_history)
        message_history.append(AIMessage(content=response.content))

        st.write("**Answer:**")
        st.success(response.content)
