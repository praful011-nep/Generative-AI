from langchain_huggingface import HuggingFaceEmbeddings

'''
    Model is locally installed and run from huggingface
'''

# Initialize Google embedding model
embeddings = HuggingFaceEmbeddings(
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
)

#Generate Embeddings
texts = [
    "Hello I am a learner",
    "This is a GenAI tutorial"
]

vector = embeddings.embed_documents(texts)

print(vector)