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
data = TextLoader("RAG noted GROQ")
print(data)