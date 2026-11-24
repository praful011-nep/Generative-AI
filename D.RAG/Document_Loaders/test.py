# To not show warnings during output
import warnings
warnings.filterwarnings('ignore')

# Load and Read Text File
from langchain_community.document_loaders import TextLoader

'''
    Document Loaders: 
    - Used to load data from different sources into LangChain and convert into standard Document format.
    - Each Document contains page_content (text) and metadata (additional information).

    Text Loader:
    - Used to load data from plain text files
    - load() is used to read the file and retriev content
'''

# Create Text Loader object and provide file path
# data is first in object form
data = TextLoader(
    r"C:\Users\prafu\Music\Generative-AI\D.RAG\Document_Loaders\RAG noted GROQ.txt",
    encoding='utf-8'
)
# print(data)

#.load() -> reads meta data and page content
docs = data.load() 

# Returns first document
'''
    .page_content -> only return page_content
    .metadata -> only return metadata
'''
print(docs[0].page_content)

