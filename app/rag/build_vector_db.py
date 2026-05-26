import pandas as pd
from langchain_core.documents import Document
from langchain_chroma import Chroma
from langchain_ollama.embeddings import OllamaEmbeddings

CODING_POLICY_FILE = "app/data/policies/coding_policy.csv"
CHROMA_DB_LOCATION = "app/data/vector_db"


df = pd.read_csv(CODING_POLICY_FILE)

doc = [
    Document(page_content=f"""
    Category: {r.category}
    Title: {r.title}
    Content: {r.content}
    Team: {r.team}
    Priority: {r.priority}
""")
    for r in df.itertuples()
]

embeddings = OllamaEmbeddings(model="nomic-embed-text:latest")

Chroma.from_documents(documents=doc, embedding=embeddings,
                      persist_directory=CHROMA_DB_LOCATION)

print("Create vector_db with our standards")
