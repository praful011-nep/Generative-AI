'''
    - Token-based splitting divides a document into chunks based on the
    number of tokens, not characters.
    - Since LLMs process tokens instead of words, this method aligns better with how models actually read text.
    - Should not exceed the token limit.
    - Same tokenizer should be used to as language model.
''' 


# Load PDF Document object 
import warnings
warnings.filterwarnings('ignore')
from langchain_community.document_loaders import PyPDFLoader

data = PyPDFLoader(r"C:\Users\prafu\Music\Generative-AI\D.RAG\Document_Loaders\Chapter9IntroductiontoMLRegression1_985a1194-056b-43c1-af86-bfa0dca9969a_268917_.pdf")

docs = data.load()

from langchain_text_splitters import TokenTextSplitter

splitter = TokenTextSplitter(
    chunk_size = 100,
    chunk_overlap = 1
)

chunks = splitter.split_documents(docs)

print(len(chunks))