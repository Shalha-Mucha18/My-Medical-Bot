import os
import time
from pathlib import Path
from dotenv import load_dotenv
from tqdm.auto import tqdm

from pinecone import Pinecone, ServerlessSpec
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# Load environment variables
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("❌ GOOGLE_API_KEY is not set. Please check your .env file or environment.")
if not PINECONE_API_KEY:
    raise ValueError("❌ PINECONE_API_KEY is not set. Please check your .env file or environment.")

PINECONE_ENV = "us-east-1"
PINECONE_INDEX_NAME = "medical-knowledge-base"

UPLOAD_DIR = Path("./uploaded_files")
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Initialize Pinecone
pinecone = Pinecone(api_key=PINECONE_API_KEY)
spec = ServerlessSpec(cloud="aws", region=PINECONE_ENV)

existing_indexes = [i['name'] for i in pinecone.list_indexes()]

if PINECONE_INDEX_NAME not in existing_indexes:
    pinecone.create_index(
        name=PINECONE_INDEX_NAME,
        dimension=768,  # Google Generative AI embeddings dimension
        metric="dotproduct",
        spec=spec
    )
    while not pinecone.describe_index(PINECONE_INDEX_NAME).status['ready']:
        time.sleep(1)

index = pinecone.Index(PINECONE_INDEX_NAME)

def load_vectorestore(uploaded_files):
    embed_model = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    file_paths = []

    # Save uploaded files
    for file in uploaded_files:
        save_path = UPLOAD_DIR / file.filename
        with open(save_path, "wb") as f:
            f.write(file.file.read())
        file_paths.append(str(save_path))

    for file_path in file_paths:
        loader = PyPDFLoader(file_path)
        documents = loader.load()

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        chunks = splitter.split_documents(documents)

        texts = [chunk.page_content for chunk in chunks]
        metadata = [chunk.metadata for chunk in chunks]
        ids = [f"{Path(file_path).stem}-{i}" for i in range(len(texts))]

        print(f"Embedding {len(texts)} chunks...")

        embeddings = embed_model.embed_documents(texts)

        print("Upserting embeddings to Pinecone...")

        vectors = list(zip(ids, embeddings, metadata))

        with tqdm(total=len(vectors), desc="Upserting to Pinecone") as progress:
            index.upsert(vectors=vectors, namespace="medical-knowledge-base")
            progress.update(len(vectors))

        print(f"✅ Finished processing {file_path}")
