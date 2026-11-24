import warnings
warnings.filterwarnings('ignore')
from langchain_community.document_loaders import PyPDFLoader

data = PyPDFLoader(r"C:\Users\prafu\Music\Generative-AI\D.RAG\Document_Loaders\Chapter9IntroductiontoMLRegression1_985a1194-056b-43c1-af86-bfa0dca9969a_268917_.pdf")

docs = data.load()

# A Document is created for each page
# print(len(docs))

# To see content of specific page
print(docs[21].page_content)

# Note: Since AI model cannot have infinite context window chunking is used to split the text for prompt