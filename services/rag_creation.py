import os
from langchain_community.vectorstores import Chroma
from agents.embeddings import embedding
from services.chunks import split_text
from langchain_core.documents import Document

CHROMA_DIR = "./chroma_db"
DATA_FILE = "services/documents.txt"

def load_chroma():
    # 🔹 Charger Chroma si elle existe
    if os.path.exists(CHROMA_DIR):
        print("✅ ChromaDB chargée")
        return Chroma(
            persist_directory=CHROMA_DIR,
            embedding_function=embedding
        )

    print("⚠️ ChromaDB absente → création")

    # 🔹 Lecture du fichier documents.txt
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        texts = [line.strip() for line in f if line.strip()]

    # 🔹 Conversion en Documents LangChain
    documents = [Document(page_content=text) for text in texts]

    # 🔹 Découpage en chunks
    chunks = []
    for doc in documents:
        chunks.extend(split_text(doc.page_content))

    # 🔹 Création ChromaDB
    db = Chroma.from_documents(
        documents=chunks,
        embedding=embedding,
        persist_directory=CHROMA_DIR
    )

    db.persist()
    return db
