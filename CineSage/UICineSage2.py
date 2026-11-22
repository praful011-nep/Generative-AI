import streamlit as st
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import List, Optional
from langchain_core.output_parsers import PydanticOutputParser
load_dotenv()

from langchain_groq import ChatGroq


model = ChatGroq(
    model='openai/gpt-oss-120b'
)


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
prompt = ChatPromptTemplate([
    (
        'system', '''
Extract movie information form the paragraph
{format_instructions}
'''
),
(
    'human', '''{paragraph}'''
)
])

st.title("Movie Information Extractor")

# paragraph is filled by the user
para = st.text_area("Give your paragraph:", height=200)

if st.button("Submit"):
    # prompt is invoked and paragraph is filled by value of para
    final_prompt = prompt.invoke(
        {'paragraph': para,
         'format_instructions': parser.get_format_instructions()
        }
    )

    response = model.invoke(final_prompt)

    st.code(response.content, language="json")