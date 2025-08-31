import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

# Load environment variables from parent folder
load_dotenv(dotenv_path="../../.env")

# Get API key
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("API key not found. Please check your .env file in the parent folder.")
else:
    client = Groq(api_key=api_key)

    # Initialize memory in Streamlit session state
    if "memory" not in st.session_state:
        st.session_state.memory = []

    st.title("Chatbot with Memory")

    # User input
    user_input = st.text_input("You:", "")

    if st.button("Send") and user_input.strip():
        # Add user input to memory
        st.session_state.memory.append({"role": "user", "content": user_input})

        # Keep only the last 5 messages
        st.session_state.memory = st.session_state.memory[-5:]

        # Send conversation to Groq API
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=st.session_state.memory
        )

        # Extract chatbot reply
        bot_reply = response.choices[0].message.content

        # Add reply to memory
        st.session_state.memory.append({"role": "assistant", "content": bot_reply})

    # Display chat history
    for message in st.session_state.memory:
        role = "You" if message["role"] == "user" else "Chatbot"
        st.write(f"**{role}:** {message['content']}")
