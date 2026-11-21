import os
from pathlib import Path
from dotenv import load_dotenv
from langchain_groq import ChatGroq


load_dotenv(Path(__file__).resolve().parents[1] / ".env", override=True)


model = ChatGroq(
    model="openai/gpt-oss-120b", 
    api_key=os.getenv("GROQ_API_KEY "), 
    timeout = 40
)

print("------------Welcome (Type 0 to exit)---------------")

while True:
    prompt = input("You: ")
    if prompt == '0':
        break
    response = model.invoke(prompt)

    print("Bot: ",response.content)
