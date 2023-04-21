import streamlit as st
from chatbot_model import *

st.header("CareBot: A Personalized and Intelligent Chatbot for Your Medical Needs")

st.markdown("""---""")

question_input = st.text_input("Enter question")
rerun_button = st.button("Rerun")

st.markdown("""---""")

with st.sidebar:
    color = st.color_picker('Pick a color', '#00FF00')

if question_input:
    response = chatbot_response(question_input)
else:
    response = None

if rerun_button:
    response = chatbot_response(question_input)
else:
    pass

if response:
    st.write("Response:", unsafe_allow_html=True)
    st.write(f"<div style='color: {color};'>{response}</div>", 
             unsafe_allow_html=True)
else:
    pass
