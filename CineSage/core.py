from dotenv import load_dotenv
from pydantic import BaseModel
from typing import List, Optional
from langchain_core.output_parsers import PydanticOutputParser
load_dotenv()

from langchain_groq import ChatGroq


model = ChatGroq(
    model = 'openai/gpt-oss-120b'
)
# response = model.invoke("Hello")
# print(response.content)


class Movie(BaseModel):
    title: str
    release_year: Optional[int]
    genre: List[str]
    director: Optional[str]
    cast: List[str]
    rating: Optional[float]
    summary: str

# Checks is the given information is in correct format or not
parser = PydanticOutputParser(pydantic_object=Movie)
'''
    Similar chatprompt cannot be written multiple times. Insead for effeciency, Prompt Templates are used.
'''
from langchain_core.prompts import ChatPromptTemplate

# Is not used as the BaseModel class gives the instruction what and how to give ouytput
# prompt = ChatPromptTemplate.from_messages([
#     ("system", """
#     You are a movie information assistant.
#     Given a movie description, provide the following information:

#     1. Movie Name
#     2. Genre
#     3. Director
#     4. Main Cast
#     5. Release Year
#     6. Plot Summary
#     7. Language

#     If any information is unavailable or cannot be
#     confidently identified, mention 'Unknown'.
#     """),

#     ("human", "Here is the movie description:\n{paragraph}")
# ])
# paragraph is filled by the user


prompt = ChatPromptTemplate(
    (
        'system', '''
Extract movie information form the paragraph
{format_instructions}
'''
),
(
    'human', '''{paragraph}'''
)
)

para = input("Give your paragraph: ")

# prompt is invoked and paragraph is filled by value of para
final_prompt = prompt.invoke(
    {'paragraph': para,
     'format_instruction': parser.get_format_instructions()
    }
)

response = model.invoke(final_prompt)

print(response.content)