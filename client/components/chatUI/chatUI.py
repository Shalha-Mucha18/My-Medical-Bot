import streamlit as st
from utils.api import ask_question
import re

# ---------------------------
# Custom CSS for styling
# ---------------------------
def add_custom_css():
    st.markdown(
        """
        <style>
            .block-container { max-width: 850px; padding-top: 1.5rem; }

            .assistant-bubble {
                background: #f3f4f6;
                color: #111827;
                border-radius: 1rem;
                padding: 1rem;
                margin: 0.5rem 0;
                text-align: left;
                white-space: pre-wrap;
                box-shadow: 0px 2px 6px rgba(0,0,0,0.1);
            }
            .user-bubble {
                background: #d1fae5;
                color: #064e3b;
                border-radius: 1rem;
                padding: 1rem;
                margin: 0.5rem 0 0.5rem auto;
                text-align: right;
                max-width: 70%;
                white-space: pre-wrap;
                box-shadow: 0px 2px 6px rgba(0,0,0,0.1);
            }
            .sources {
                font-size: 0.85rem;
                color: #374151;
                margin-top: 0.5rem;
            }
            .sources a {
                color: #2563eb;
                text-decoration: none;
            }
            .sources a:hover {
                text-decoration: underline;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


# ---------------------------
# Helper to format responses
# ---------------------------
def format_response(text: str) -> str:
    """
    Format assistant responses:
    - If short, return as-is.
    - If long, split into intro + bullet points.
    - If very long, wrap extra in an expander.
    """
    words = text.split()
    if len(words) <= 40:
        return text  # short, keep as-is

    # Split into lines
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    intro = lines[0]  # first line = intro
    bullets = [f"- {line}" for line in lines[1:]]

    formatted = f"**{intro}**\n\n" + "\n".join(bullets[:5])

    # Add expander for extra bullets
    if len(bullets) > 5:
        extra = "\n".join(bullets[5:])
        formatted += f"\n\n<details><summary>Read more</summary>\n\n{extra}\n\n</details>"

    return formatted


# ---------------------------
# Chat UI
# ---------------------------
def render_chat():
    # st.set_page_config(page_title="Medical Chatbot", page_icon="💬", layout="centered")
    add_custom_css()

    # Title
    # st.title("💬 Medical Chatbot")
    st.caption("Ask anything. Upload knowledge docs. Get clear, concise answers.")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Render chat history
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(f"<div class='user-bubble'>{msg['content']}</div>", unsafe_allow_html=True)
        else:
            text = format_response(msg["content"])
            if "sources" in msg and msg["sources"]:
                src_html = "<div class='sources'><b>Sources</b><br>" + "<br>".join(
                    f"<a href='{s}' target='_blank'>{s}</a>" for s in msg["sources"]
                ) + "</div>"
                text += src_html
            st.markdown(f"<div class='assistant-bubble'>{text}</div>", unsafe_allow_html=True)

    # Input box
    user_input = st.chat_input("Type your question...")

    if user_input:
        # Show user message
        st.markdown(f"<div class='user-bubble'>{user_input}</div>", unsafe_allow_html=True)
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Call backend API
        try:
            response = ask_question(user_input)

            if response.status_code == 200:
                data = response.json()
                raw_answer = data.get("response", "No response")
                sources = data.get("sources", [])

                answer = format_response(raw_answer)

                st.markdown(f"<div class='assistant-bubble'>{answer}</div>", unsafe_allow_html=True)
                st.session_state.messages.append(
                    {"role": "assistant", "content": raw_answer, "sources": sources}
                )
            else:
                st.error(f"Error {response.status_code}: {response.text}")

        except Exception as e:
            st.error(f"Request failed: {e}")


# if __name__ == "__main__":
#     render_chat()






