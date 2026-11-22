from dotenv import load_dotenv

load_dotenv()

from langchain_groq import ChatGroq

model = ChatGroq(
    model = 'openai/gpt-oss-120b'
)
# response = model.invoke("Hello")
# print(response.content)

'''
    Similar chatprompt cannot be written multiple times. Insead for effeciency, Prompt Templates are used.
'''
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", """
    You are a movie information assistant.
    Given a movie description, provide the following information:

    1. Movie Name
    2. Genre
    3. Director
    4. Main Cast
    5. Release Year
    6. Plot Summary
    7. Language

    If any information is unavailable or cannot be
    confidently identified, mention 'Unknown'.
    """),

    ("human", "Here is the movie description:\n{paragraph}")
])
# paragraph is filled by the user
