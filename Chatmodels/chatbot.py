import os
from pathlib import Path
from dotenv import load_dotenv
from langchain_groq import ChatGroq


load_dotenv(Path(__file__).resolve().parents[1] / ".env", override=True)

# Initialize model from API
model = ChatGroq(
    model="openai/gpt-oss-120b", 
    api_key=os.getenv("GROQ_API_KEY "), 
    timeout = 40
)

# Stores all the proompts and responses from user and Bot side
messages = [

]
print("------------Welcome (Type 0 to exit)---------------")

# Conversation can be till desired,
while True:
    prompt = input("You: ")
    messages.append(prompt)
    if prompt == '0':
        break
    response = model.invoke(messages) #Store response from model
    messages.append(response.content)
    print("Bot: ",response.content)
