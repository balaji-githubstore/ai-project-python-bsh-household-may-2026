from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

CHROMA_DB_LOCATION = "app/data/vector_db"

def retrieve_rules(query: str):
    embeddings = OllamaEmbeddings(model="nomic-embed-text:latest")
    db = Chroma(persist_directory=CHROMA_DB_LOCATION,
                embedding_function=embeddings)
    retriever = db.as_retriever(search_kwargs={"k": 5})
    docs = retriever.invoke(query)
    rules = ("\n".join([doc.page_content for doc in docs]))
    return rules


# print(retrieve_rules("selenium"))