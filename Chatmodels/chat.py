import os
from pathlib import Path
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv(Path(__file__).resolve().parents[1] / ".env", override=True)

model_groq = init_chat_model(
    "groq:openai/gpt-oss-120b",
    api_key=os.getenv("GROQ_API_KEY")
)

response = model_groq.invoke("Hello")
# print(response.content)
model_gemini = ChatGoogleGenerativeAI(model="gemini-3.8-flash", api_key=os.getenv("GOOGLE_API_KEY "), timeout = 40)
response = model_gemini.invoke("Who are you?")
