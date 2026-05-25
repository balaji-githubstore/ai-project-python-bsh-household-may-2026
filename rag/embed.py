"""
pip install pandas langchain-core langchain-chroma langchain-text-splitters langchain-ollama 

"""


import pandas as pd
from langchain_core.documents import Document
from langchain_chroma import Chroma
from langchain_ollama.embeddings import OllamaEmbeddings


df = pd.read_csv("policies\coding_policy.csv")

doc = [
    Document(page_content=f"""
    Category: {r.category}
    Rule: {r.rule}
    Severity: {r.severity}
    Example: {r.example}
""")
    for r in df.itertuples()
]

embeddings=OllamaEmbeddings(model="nomic-embed-text:latest")

Chroma.from_documents(documents=doc,embedding=embeddings,persist_directory="rag/vector_db")

print("Create vector_db with our standards")

