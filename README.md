# 🩺 Health Assistant Chatbot  

![Python](https://img.shields.io/badge/Python-3.11-blue) ![FastAPI](https://img.shields.io/badge/FastAPI-Backend-success) ![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red) ![LLM](https://img.shields.io/badge/LLM-Groq%20LLaMA3--70B-purple) ![RAG](https://img.shields.io/badge/RAG-Enabled-brightgreen) ![Pinecone](https://img.shields.io/badge/VectorDB-Pinecone-blueviolet) ![Embeddings](https://img.shields.io/badge/Embeddings-Google%20GenAI%20%2F%20BGE-orange) ![Demo](https://img.shields.io/badge/Demo-Coming%20Soon-lightgrey) ![License](https://img.shields.io/badge/License-MIT-green)



A **Medical Domain Chatbot** powered by **Retrieval-Augmented Generation (RAG)**.  
This application helps users query their **own medical documents** (PDFs such as textbooks, reports, research papers, or clinical guidelines) to get contextually accurate and concise answers.  

Instead of relying only on pre-trained models, this chatbot intelligently **retrieves relevant knowledge** from uploaded files, embeds them in a **vector database**, and uses a **large language model (LLM)** to generate answers.  

---

## 🌟 Motivation  

- Healthcare professionals and students often need **quick, reliable answers** from lengthy resources.  
- Traditional chatbots lack **domain-specific accuracy** and cannot incorporate **private data**.  
- This project bridges the gap by combining **RAG with domain expertise**, enabling **personalized, document-grounded medical assistance**.  

---
<img width="1893" height="854" alt="Screenshot 2025-08-24 002414" src="https://github.com/user-attachments/assets/7d26b579-b911-4b2d-95e9-84dd1a57ea38" />

## ✨ Features  

1. Upload and query **multiple PDFs** (textbooks, notes, guidelines, reports).  
2. **Semantic chunking** — large PDFs are split into context-preserving sections.  
3. Embeddings generated using **Google Generative AI / BGE** for high-quality vector representation.  
4. **Scalable vector search** with **Pinecone DB**.  
5. **API-first backend** (FastAPI) with endpoints for:  
   - File upload  
   - Vector store updates  
   - Q&A over documents  
6. Modern **Streamlit chat UI** with chat history and source references.  

---

## ⚙️ Tech Stack  

| Component      | Technology Used                  |
| -------------- | -------------------------------- |
| **LLM**        | **LLaMA3-70B**      |
| **Embeddings** | Google Generative AI / BGE       |
| **Vector DB**  | Pinecone                         |
| **Framework**  | LangChain                        |
| **Backend**    | FastAPI                          |
| **Frontend**   | Streamlit (chat UI)              |

---
## 📁 Folder Structure

```bash
└── 📁client                # Streamlit frontend
    └── 📁components        # UI components
        ├── chatUI.py       # Chat interface
        ├── history.py      # Chat history
        ├── upload.py       # File upload UI
    └── 📁utils             # API helpers
        ├── api.py
    ├── app.py              # Streamlit app entry
    ├── config.py           # Client config
    └── requirements.txt    # Client dependencies

└── 📁server                # FastAPI backend
    └── 📁middlewares       # Error & exception handling
        ├── exception_handlers.py
    └── 📁modules           # Core logic
        ├── llm.py          # LLM integration
        ├── vectorstore.py  # Pinecone DB integration
        ├── pdf_manage.py   # PDF parsing & chunking
        ├── query_manage.py # Query processing
    └── 📁routes            # API routes
        ├── ask_question.py
        ├── upload_pdfs.py
    └── 📁uploaded_docs     # Uploaded PDFs storage
    ├── main.py             # FastAPI entry point
    ├── logger.py           # Custom logging
    ├── requirements.txt    # Backend dependencies
    └── test.py             # Tests
```

## Quick Setup

1. Clone the repo
```bash
git clone https://github.com/Shalha-Mucha18/RAGMed
cd RAGMed

```
2. Backend Setup
```bash
cd server

# Create virtual env
uv venv
.venv/bin/activate     # Windows: venv\Scripts\activate

# Install dependencies
uv pip install -r requirements.txt

# Set environment variables (.env)
GOOGLE_API_KEY=...
GROQ_API_KEY=...
PINECONE_API_KEY=...

# Run backend
uvicorn main:app --reload
```
3. Frontend Setup
```bash
cd ../client

# Create virtual env
uv venv
.venv/bin/activate     # Windows: venv\Scripts\activate

# Install dependencies
uv pip install -r requirements.txt

# Run frontend
streamlit run app.py
```
## 🌟 Credits

- Built with inspiration from LangChain, Groq, Pinecone, and FastAPI ecosystems.

## 🎉 License

This project is licensed under the MIT License
.
You are free to use, modify, and distribute this software with attribution.

---




