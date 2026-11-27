# To not show warnings during output
import warnings
warnings.filterwarnings('ignore')

# Load and Read Text File
from langchain_community.document_loaders import TextLoader

# data is first in object form
data = TextLoader(
    r"C:\Users\prafu\Music\Generative-AI\D.RAG\Document_Loaders\RAG noted GROQ.txt",
    encoding='utf-8'
)

docs = data.load() 

# print(docs[0].page_content)

# Import CharacterTextSplitter to split documents into smaller chunks
from langchain_text_splitters import CharacterTextSplitter

'''
    Create a text splitter with chunk size and overlap
    - chunk_size: Defines the maximum number of characters allowed in   each text chunk.
    - chunk_overlap: Defines the number of characters repeated between consecutive chunks to preserve context.
'''

#Create splitter object
splitter = CharacterTextSplitter(
    chunk_size = 10,
    chunk_overlap = 1 
)

# Split the loaded documents into smaller chunks
chunks = splitter.split_documents(docs)

print(len(chunks))