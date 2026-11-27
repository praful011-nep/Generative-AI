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