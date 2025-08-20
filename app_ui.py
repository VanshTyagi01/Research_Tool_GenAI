from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate, load_prompt
import streamlit as st

load_dotenv()
model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')
st.header("Research Tool")

paper_input = st.text_input("Enter title of the Research Paper")

style_input = st.selectbox("Select Explanation Style", ["Begineer-Friendly", "Technical", "Code-Oriented", "Mathematical"])

length_input = st.selectbox("Select Explanation length", ["short(1-2 Paragraph)", "Medium (3-5 paragraph)", "Long (Detailed Explanation)"])

template = load_prompt('D:/langchain_models/LangChain_Prompts_WorkFlow/template.json')


# user_input = st.text_input("Enter your prompt")
if st.button('Summarize'):
    # making chain to reducr invoke times
    chain = template | model
    result = chain.invoke({
        'paper_input':paper_input,
        'style_input':style_input,
        'length_input':length_input
    })
    
    # result = model.invoke(prompt)
    st.write(result.content)