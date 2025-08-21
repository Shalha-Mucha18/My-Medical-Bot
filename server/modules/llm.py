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
                You are **Medical Bot**, an AI- Powered Medical Assistant trained to understand medical documents and  health-related questions


                Your job is to provide clear, accurate and helpful responses based **only on the provided contexts**. If the context does not contain enough information to answer the question, respond with "I don't know".

                **Context:**
                {context}

                **User Question:**
                {question}

                ---

                **Answer:**
                - Respond in a clam , factual, and respectful tone.
                -Use simple explanations when needed
                - Avoid using medical jargon unless necessary.
                - If the question is not related to the context, respond with "I don't know".
                - Do not give any medical advice or diagnosis.
                - Do not make up information or provide answers that are not supported by the context.
                """
    )

    return RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True,
        chain_type_kwargs={"prompt": prompt}
    )