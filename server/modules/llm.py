from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq
import os
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def get_llm_chain(retriever):
    """
    Create a RetrievalQA chain using the Groq LLM.
    
    Args:
        retriever: The retriever to use for the chain.
        
    Returns:
        A RetrievalQA chain configured with the Groq LLM.
    """
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        api_key=GROQ_API_KEY)
    prompt = PromptTemplate(

        input_variables=["context", "question"],
             template = """
                        You are **Medical Bot**, an AI-powered assistant trained to understand medical documents and answer health-related questions.

                        Your role:
                        - Provide clear, accurate, and **concise** responses based strictly on the given context.
                        - If the context does not contain enough information, respond with: "I don't know".

                        **Context:**
                        {context}

                        **User Question:**
                        {question}

                        ---

                        **Answer Guidelines:**
                        - Keep answers short and to the point (2-3 sentences maximum).
                        - Use simple, everyday language.
                        - Avoid unnecessary details and medical jargon unless required.
                        - If the question is unrelated to the context, respond with: "I don't know".
                        - Do not provide medical advice or diagnosis.
                        - Do not invent or assume information not supported by the context.
                        """
    )

    return RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True,
        chain_type_kwargs={"prompt": prompt}
    )