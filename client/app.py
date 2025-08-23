import streamlit as st

from components.upload import render_uploader

from components.history import render_history_download

from components.chatUI.chatUI import render_chat

st.set_page_config(page_title= "Medical Bot", layout="wide")

st.title("Medical Chatbot") 


render_uploader()
render_chat()
render_history_download()

