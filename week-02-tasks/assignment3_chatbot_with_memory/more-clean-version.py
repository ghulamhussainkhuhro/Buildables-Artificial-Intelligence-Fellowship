import os
from pathlib import Path
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

# Load .env from parent folder (two levels up: assignment -> week2 -> parent)

load_dotenv(dotenv_path="../../.env")

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    st.error("API key not found. Please check the .env file in the parent folder.")
    st.stop()

client = Groq(api_key=api_key)

# Page config
st.set_page_config(page_title="Chatbot with Memory", layout="centered")

# Initialize memory (list of dicts with keys: role, content)
if "memory" not in st.session_state:
    st.session_state.memory = []

# UI header and controls
st.title("Chatbot with Memory")

col1, col2 = st.columns([1, 3])
with col1:
    if st.button("New chat"):
        st.session_state.memory = []

# Input: prefer st.chat_input; fallback to text_input + Send button
user_message = None
if hasattr(st, "chat_input"):
    # chat_input automatically clears after submit
    user_message = st.chat_input("Type your message and press Enter...")
else:
    # fallback layout for older Streamlit versions
    input_col, send_col = st.columns([4, 1])
    with input_col:
        # store text in session_state so we can clear after send
        if "fallback_input" not in st.session_state:
            st.session_state.fallback_input = ""
        st.session_state.fallback_input = st.text_input("You:", st.session_state.fallback_input, key="fallback_input_box")
    with send_col:
        send_clicked = st.button("Send")
    if send_clicked and st.session_state.get("fallback_input", "").strip():
        user_message = st.session_state["fallback_input"].strip()
        # clear fallback input for next run
        st.session_state["fallback_input"] = ""

# When user submits a message
if user_message:
    # append user message
    st.session_state.memory.append({"role": "user", "content": user_message})
    # enforce memory limit BEFORE sending (keep last 5)
    st.session_state.memory = st.session_state.memory[-5:]

    # send to Groq
    try:
        with st.spinner("Waiting for reply..."):
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=st.session_state.memory
            )
        bot_reply = response.choices[0].message.content
    except Exception as e:
        bot_reply = f"[Error communicating with API] {e}"
        st.error(bot_reply)

    # append bot reply and again enforce memory size
    st.session_state.memory.append({"role": "assistant", "content": bot_reply})
    st.session_state.memory = st.session_state.memory[-5:]

# Display chat history using chat_message if available
if hasattr(st, "chat_message"):
    for msg in st.session_state.memory:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])
else:
    # fallback display
    for msg in st.session_state.memory:
        label = "You" if msg["role"] == "user" else "Chatbot"
        st.write(f"**{label}:** {msg['content']}")
