from dotenv import load_dotenv

load_dotenv()

from langchain_groq import ChatGroq

model = ChatGroq(
    model = 'openai/gpt-oss-120b'
)
response = model.invoke("Hello")
print(response.content)