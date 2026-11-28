# Load PDF Document object 
import warnings
warnings.filterwarnings('ignore')
from langchain_community.document_loaders import PyPDFLoader

data = PyPDFLoader(r"C:\Users\prafu\Music\Generative-AI\D.RAG\Document_Loaders\Chapter9IntroductiontoMLRegression1_985a1194-056b-43c1-af86-bfa0dca9969a_268917_.pdf")

docs = data.load()

'''
    ----------------------------------- Recursive Character Text Splitting -----------------------------------

    - RecursiveCharacterTextSplitter divides documents into smaller chunks using a hierarchy of separators.

    - It tries to split text using the following separators in order:
      ["\n\n", "\n", " ", ""]

      1. "\n\n" -> Paragraph breaks
      2. "\n"   -> Line breaks
      3. " "    -> Spaces between words
      4. ""     -> Individual characters (last resort)

    - It first tries larger natural boundaries (paragraphs) and gradually
      moves to smaller boundaries if the chunk size is exceeded.

    - Chunk Size defines the maximum size of each chunk.
    - Chunk Overlap maintains shared text between consecutive chunks
      to preserve context.

    - It tries to keep sentences and paragraphs together whenever possible.
'''

from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 10
)

chunks = splitter.split_documents(docs)

print(chunks[0].page_content)