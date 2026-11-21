from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
)

texts = [
    "Hello I am a learner",
    "This is a GenAI tutorial"
]

vector = embeddings.embed_documents(texts)

print(vector)