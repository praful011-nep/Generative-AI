import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
import warnings 
warnings.filterwarnings('ignore')
from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import ChatPromptTemplate


load_dotenv()

# Document Object
data = TextLoader(
    r"C:\Users\prafu\Music\Generative-AI\D.RAG\Document_Loaders\RAG noted GROQ.txt",
    encoding='utf-8'
)
# Loaded Object content
docs = data.load()

# Create a prompt template
ChatPromptTemplate.from_messages([
    ('system','Your are a AI that summarizes text.'),
    ('human','{data}')
])
# Initialize model using API keu
model = ChatGroq(
    model="openai/gpt-oss-120b", 
    api_key=os.getenv("GROQ_API_KEY "), 
    timeout = 40
)