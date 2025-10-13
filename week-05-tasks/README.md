# Mini RAG Application – Week 05

## Overview

This project implements a simple **Retrieval-Augmented Generation (RAG)** application using **Streamlit**.
It allows users to upload a **PDF or DOCX** file, automatically extract and store the document text as vector embeddings in **Pinecone**, and then ask natural language questions about the uploaded content using a **Groq LLM** (Llama 3.3 model).

The app demonstrates a complete mini RAG pipeline, from document ingestion to retrieval and response generation.

---

## Features

* Upload and process PDF or DOCX files
* Automatic text extraction and chunking
* Vector embeddings generated using **Hugging Face Sentence Transformer**
* Semantic search powered by **Pinecone**
* Question answering with **Groq Llama-3.3-70B-Versatile**
* Simple, clean Streamlit interface

---

## Project Structure

```
BUILDABLE_AI/
│
├── week-01-tasks/
├── week-02-tasks/
├── week-03-tasks/
├── week-04-tasks/
├── week-05-tasks/
│   ├── app.py                # Streamlit RAG app
│   ├── README.md             # This file
│   └── text.pdf (optional)   # Example document
│
├── .env
├── requirements.txt
└── README.md
```

---

## Environment Setup

### 1. Create and Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate       # for Linux/Mac
venv\Scripts\activate          # for Windows
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Add Environment Variables

Create a `.env` file in the root directory and include the following keys:

```
GROQ_API_KEY=your_groq_api_key
PINECONE_API_KEY=your_pinecone_api_key
```

---

## How to Run the Application

1. Navigate to the `week-05-tasks` directory.
2. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```
3. The app will open in your browser.
4. Upload a PDF or DOCX file.
5. Ask any question related to the uploaded document.

---

## How It Works

1. **Document Upload**
   The user uploads a file, which is temporarily saved and processed.

2. **Text Extraction and Chunking**
   The document text is extracted using `PyMuPDF` (for PDFs) or `python-docx` (for DOCX files).
   It is split into overlapping chunks using `RecursiveCharacterTextSplitter`.

3. **Embedding Generation**
   Each text chunk is converted into a numerical vector using the Hugging Face model
   `sentence-transformers/all-MiniLM-L6-v2`.

4. **Vector Storage**
   The embeddings are stored in a **Pinecone** vector index for efficient semantic retrieval.

5. **Question Answering (RAG)**
   When a user enters a query:

   * The top-k relevant chunks are retrieved from Pinecone.
   * The context is passed to the **Groq LLM (Llama-3.3-70B-Versatile)**.
   * The model generates an answer based only on the retrieved context.

---

## Key Technologies

* **Streamlit** – Web interface
* **LangChain** – Framework for LLM pipelines
* **Groq API** – Large Language Model inference
* **Pinecone** – Vector database
* **Hugging Face Embeddings** – Text vectorization
* **PyMuPDF / python-docx** – Document parsing

---

## Example Queries

After uploading a document, you can try questions like:

* “What is the main topic of this document?”
* “Who is mentioned as the author?”
* “Summarize the second section.”
* “When did the described event take place?”

---

## Notes

* The app creates or reuses a Pinecone index named `week5-rag-app`.
* Uploaded files are stored temporarily during runtime only.
* If you re-upload a file, the index is overwritten with new vectors.

---

## Author

Developed by **Ghulam Hussain Khuhro**
For **Week-05 Assignment — Buildable AI Fellowship**

