'''
            IMPLEMENTATION OF CONCEPTS USED
'''
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
import warnings 
warnings.filterwarnings('ignore')
from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import ChatPromptTemplate


load_dotenv()

# Document Object
datatxt = TextLoader(
    r"C:\Users\prafu\Music\Generative-AI\D.RAG\Document_Loaders\RAG noted GROQ.txt",
    encoding='utf-8'
)

datapddf = PyPDFLoader(r"C:\Users\prafu\Music\Generative-AI\D.RAG\Document_Loaders\Chapter9IntroductiontoMLRegression1_985a1194-056b-43c1-af86-bfa0dca9969a_268917_.pdf")

url = 'https://www.gsmarena.com/google_pixel_11_pro_5g-14801.php'
dataurl = WebBaseLoader(url)

data= PyPDFLoader(r"C:\Users\prafu\Music\Generative-AI\D.RAG\Document_Loaders\deeplearning.pdf")

# Loaded Object content
docstxt = datatxt.load()
docspdf = datapddf.load()
docsurl = dataurl.load()
docs = data.load()


# Create a prompt template
template = ChatPromptTemplate.from_messages([
    ('system','Your are a AI that summarizes text.'),
    ('human','{data}')
])

# Insert document content in prompt
prompttxt = template.format_messages(data = docstxt[0].page_content)
promptpdf = template.format_messages(data = docspdf[0].page_content)
prompturl = template.format_messages(data = docsurl[0].page_content)
prompt = template.format_messages(data= docs)

# Initialize model using API keu
model = ChatGroq(
    model="openai/gpt-oss-120b", 
    api_key=os.getenv("GROQ_API_KEY"), 
    timeout = 40
)

result = model.invoke(prompt)
print(result.content)