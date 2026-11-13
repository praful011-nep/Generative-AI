import os
from pathlib import Path
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv(Path(__file__).resolve().parents[1] / ".env", override=True)

model = init_chat_model(
    "groq:openai/gpt-oss-120b",
    api_key=os.getenv("GROQ_API_KEY")
)

response = model.invoke("Hello")
print(response.content)