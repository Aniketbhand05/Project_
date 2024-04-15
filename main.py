## Integrate our code OpenAI API
import os
from constants import openai_key
from langchain.llms import OpenAI

import streamlit as st

os.environ["OPENAI_API_KEY"]=openai_key

# streamlit framework

st.title('Recipie Demo')
input_text=st.text_input("Search the recipie u want")
input_text_final = 'i want to make the ' + input_text + ' so please suggest me the reciepe for that'
## OPENAI LLMS
llm=OpenAI(temperature=0.8)



if input_text:
    st.write(llm(input_text_final))
