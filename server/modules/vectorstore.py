import os
import time
from pathlib import Path
from dotenv import load_dotenv
from tqdm.auto import tqdm
from pinecone import Pinecone,ServerlessSpace
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google import GoogleGenerativeAIEmbeddings

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

PINECONE_ENV = "us-east-1"
PINECONE_INDEX_NAME = "medical-knowledge-base"

os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

UPLOAD_DIR = Path("./uploaded_files")
os.makedirs(UPLOAD_DIR, exist_ok=True)

# initialize Pinecone
pinecone = Pinecone(
    api_key=PINECONE_API_KEY)
spec = ServerlessSpace(cloud="aws", region=PINECONE_ENV)
existing_indexes = [i['name'] for i in pinecone.list_indexes()]

if PINECONE_INDEX_NAME not in existing_indexes:
    pinecone.create_index(
        name=PINECONE_INDEX_NAME,
        dimension=768,  # Dimension for Google Generative AI embeddings
        metric="dotproduct",
        spec=spec
    )
    while not pinecone.describe_index(PINECONE_INDEX_NAME).status['ready']:
      
        time.sleep(1)

index = pinecone.Index(PINECONE_INDEX_NAME)

def load_vectorestore(uploaded_files):

    embed_model = GoogleGenerativeAIEmbeddings(
        model_name="models/embedding-001")
    file_paths = []

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
        metadata = [chunks.metadata for chunk in chunks]
        ids=[f"{Path(file_path).stem}-{i}" for i in range(texts)]

        print(f"Embedding chunks")

        embeddings = embed_model.embed_documents(texts)

        print("upserting embedding to Pinecone")

        with tqdm(total=len(texts), desc="Upserting to Pinecone") as progress:
            index.upsert(
                vectors=zip(ids, embeddings, metadata),
                namespace="medical-knowledge-base"
            )
            progress.update(len(embeddings))
        print(f"Finished processing {file_path}")






  
