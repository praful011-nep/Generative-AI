'''
                    WORKING WITH WEB PAGES
'''
from langchain_community.document_loaders import WebBaseLoader

#URl is given to create Document Object
# For multiple urls, can be stored in list and iterate it
url = 'https://www.gsmarena.com/google_pixel_11_pro_5g-14801.php'
data = WebBaseLoader(url)

# load data from source
docs = data.load()

# One Document is created for a single page
# print(len(docs))

print(docs[0].page_content)