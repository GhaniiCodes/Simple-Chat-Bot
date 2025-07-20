import os
from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser

# Streamlit UI
st.header("Translator")
st.markdown("""Need Translation?  
Select a Language and Enter Your Text""")

# Load environment variables
load_dotenv(dotenv_path=r"D:\PYTHON\GENERATIVE AI\.ENV FILES\Simple ChatBot\.env")
Groq_API_Key = os.getenv("GROQ_API_KEY")

# Model
Model = ChatGroq(model= "llama-3.1-8b-instant", groq_api_key=Groq_API_Key)

# UI Inputs
Language = ["Spanish", "French", "Italian", "German", "Polish"]
Selected_Language = st.selectbox("Select Language", Language)
Text = st.text_area("Enter Your Text to be Translated")

# Prompt
Messages = [
    SystemMessage(content=f"Translate The sentences into {Selected_Language}"),
    HumanMessage(content= Text)
]


if st.button("Translate"):
    if Text.strip() == "":
        st.warning("Please enter text to translate.")
    else:
        Outparser = StrOutputParser()
        Chain = Model | Outparser
        Response = Chain.invoke(Messages)
        st.subheader("Translated Text:")
        st.write(Response)

