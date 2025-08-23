import os
from groq import Groq
from dotenv import load_dotenv

# Load .env file (from parent folder)
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {"role": "user", "content": "Explain the importance of fast language models"},
    ],
    model="llama-3.3-70b-versatile",
)

print(chat_completion.choices[0].message.content)
