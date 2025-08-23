import streamlit as st

def render_history_download():
    # Initialize chat history if not present
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Only show download button if there are messages
    if st.session_state.messages:
        chat_text = "\n\n".join(
            [f"{m['role'].upper()}: {m['content']}" for m in st.session_state.messages]
        )
        st.download_button(
            "Download Chat History",
            chat_text,
            file_name="chat_history.txt",
            mime="text/plain"
        )
