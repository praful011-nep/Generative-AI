# Google Generative AI Embeddings
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv() # load API key from .env

# Initialize Google embedding model
embeddings = GoogleGenerativeAIEmbeddings(
    model = 'gemini-embedding-2',
    output_dimensionality= 768
)

