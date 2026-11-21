import os
from pathlib import Path
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv(Path(__file__).resolve().parents[1] / ".env", override=True)


model_gemini = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash", 
    api_key=os.getenv("GOOGLE_API_KEY "), 
    timeout = 40
)

