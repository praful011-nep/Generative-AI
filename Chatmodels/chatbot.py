import os
from pathlib import Path
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv(Path(__file__).resolve().parents[1] / ".env", override=True)


model = ChatGroq(
    model="openai/gpt-oss-120b", 
    api_key=os.getenv("GROQ_API_KEY "), 
    timeout = 40
)

prompt = input("You: ")

response = model.invoke(prompt)

print("Bot: ",response.content)
