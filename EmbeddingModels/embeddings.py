# Google Generative AI Embeddings
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv() # load API key from .env

# Initialize Google embedding model
embeddings = GoogleGenerativeAIEmbeddings(
    model = 'gemini-embedding-2',
    output_dimensionality= 768
)

# Generate Embeddings
'''
    embed_document -> used for more than 1 sentence (ask multiple things)
    embed_query -> used for 1 sentence (ask one thing)
'''
# For single text query
vector1 = embeddings.embed_query("Learning GenAI")

print(vector1)

