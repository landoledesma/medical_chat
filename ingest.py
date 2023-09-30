from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader,DirectoryLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from dotenv import load_dotenv
import os
import time 

load_dotenv("token.env")
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

DATA_PATH = "data/"
DB_FAISS_PATH = "vectorstore/db_faiss"


def create_vectordb():
    embeddings = OpenAIEmbeddings()
    loader = DirectoryLoader(DATA_PATH,glob='*.pdf',loader_cls=PyPDFLoader)
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=100,
        chunk_overlap = 100
    )
    texts = text_splitter.split_documents(documents)

    db = FAISS.from_documents(texts,embeddings)
    db.save_local(DB_FAISS_PATH)

if __name__ == "__main__":
    start_time = time.time()
    create_vectordb()
    end_time = time.time()  
    elapsed_time = end_time - start_time  # Calcula la diferencia de tiempo
    print(f"Se ha creado exitosamente la base de datos vectorial en {elapsed_time:.2f} segundos")