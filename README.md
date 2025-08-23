## 🩺 Health Assistant Chatbot

A Medical Domain Chatbot powered by Retrieval-Augmented Generation (RAG).
This application helps users query their own medical documents (PDFs such as textbooks, reports, research papers, or clinical guidelines) to get contextually accurate and concise answers.Instead of relying only on pre-trained models, this chatbot intelligently retrieves relevant knowledge from uploaded files, embeds them in a vector database, and uses a large language model (LLM) to generate answers.


### 🌟 Motivation

- Healthcare professionals and students often need quick, reliable answers from lengthy resources.

- Traditional chatbots lack domain-specific accuracy and cannot incorporate private data.

- This project bridges the gap by combining RAG with domain expertise, enabling personalized, document-grounded medical assistance.

### ✨ Features
1.  Upload and query multiple PDFs (textbooks, notes, guidelines, reports).
2. Semantic chunking — large PDFs are split into context-preserving sections.
3. Embeddings generated using Google Generative AI / BGE for high-quality vector representation.
4. Scalable vector search with Pinecone DB.
5. API-first backend (FastAPI) with endpoints for:
    - File upload
    - Vector store updates
    - Q&A over documents

### ⚙️ Tech Stack
| Component      | Technology Used                  |
| -------------- | -------------------------------- |
| **LLM**        | Groq API (**LLaMA3-70B**)        |
| **Embeddings** | Google Generative AI / BGE       |
| **Vector DB**  | Pinecone                         |
| **Framework**  | LangChain                        |
| **Backend**    | FastAPI                          |
| **Frontend**   | Streamlit (chat UI)              |

### 📁 Folder Structure
```bash

└── 📁client
    └── 📁__pycache__
        ├── config.cpython-311.pyc
    └── 📁components 
        ├── chatUI.py
        ├── history.py
        ├── upload.py
    └── 📁utils
        └── 📁__pycache__
            ├── api.cpython-311.pyc
        ├── api.py
    ├── app.py
    ├── config.py
    └── requirements.txt
└── 📁server
    └── 📁__pycache__
        
    └── 📁middlewares
        ├── exception_handlers.py
    └── 📁modules
        ├── llm.py
        ├── vectorstore.py
        ├── pdf_manage.py
        ├── query_manage.py
    └── 📁routes
        ├── ask_question.py
        ├── upload_pdfs.py
    └── 📁uploaded_docs
        ├── first.pdf
    ├── .env
    ├── logger.py
    ├── main.py
    ├── requirements.txt
    └── test.py

```

### Quick Setup
```bash
# Clone the repo
$ git clone https://github.com/Shalha-Mucha18/RAGMed
$ cd RAGMed/server

# Create virtual env
$ uv venv
$ .venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
$ uv pip install -r requirements.txt

# Set environment variables (.env)
GOOGLE_API_KEY=...
GROQ_API_KEY=...
PINECONE_API_KEY=...

# Run the server
$ uvicorn main:app --reload 


$ cd RAGMed/client

# Create virtual env
$ uv venv
$ .venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
$ uv pip install -r requirements.txt

# Run the server
$ streamlit run app.py
```
### 🌟 Credits

1. This project was inspired by the amazing work from the LangChain, Groq, Pinecone, and FastAPI ecosystems.

### 🎉 License
This project is licensed under the MIT License.
You are free to use, modify, and distribute this software, provided that proper attribution is given.




