# Load PDF Document object 
import warnings
warnings.filterwarnings('ignore')
from langchain_community.document_loaders import PyPDFLoader

data = PyPDFLoader(r"C:\Users\prafu\Music\Generative-AI\D.RAG\Document_Loaders\Chapter9IntroductiontoMLRegression1_985a1194-056b-43c1-af86-bfa0dca9969a_268917_.pdf")

docs = data.load()



from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 10
)

chunks = splitter.split_documents(docs)

print(chunks[0].page_content)