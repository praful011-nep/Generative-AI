import os
from pathlib import Path
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

load_dotenv(Path(__file__).resolve().parents[1] / ".env", override=True)

# Initialize model from API
model = ChatGroq(
    model="openai/gpt-oss-120b", 
    api_key=os.getenv("GROQ_API_KEY "), 
    timeout = 40
)

'''
    Storing responses from user and chatbot in list or even dictionary can be ineffective incase of long conversation. (memory problem/ high token usage/ no role seperation)

    langchain provides 'message' to handle that
'''
# Stores all the proompts and responses from user and Bot side (short term memory)
messages = [
    SystemMessage(content='You are a funny AI agent.')
]
print("------------Welcome (Type 0 to exit)---------------")

# Conversation can be till desired,
# while True:
#     prompt = input("You: ")
#     messages.append(prompt)
#     if prompt == '0':
#         break
#     response = model.invoke(messages) #Store response from model
#     messages.append(response.content)
#     print("Bot: ",response.content)

while True:
    prompt = input("You: ")
    # Message given by user is stored
    messages.append(HumanMessage(content=prompt))
    if prompt == '0':
        break
    response = model.invoke(messages) #Store response from model
    messages.append(AIMessage(content=response.content))
    print("Bot: ",response.content)

