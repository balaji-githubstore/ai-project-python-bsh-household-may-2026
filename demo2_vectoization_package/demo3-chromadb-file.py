import chromadb
import pandas as pd


# creates a local db file with the collection added. 
client=chromadb.PersistentClient(path="./db/coding_standard")

try:
    client.delete_collection("coding-notes")
except:
    pass

collection=client.get_or_create_collection(name="coding-notes")

df=pd.read_csv("files/datadb.csv")
# print(df["id"].astype(str).tolist())
# print(df["content"].tolist())

collection.add(
    ids=df["id"].astype(str).tolist(),
    documents=df["content"].tolist()
)

result=collection.query(
    query_texts=["how should selectors be written?"],
    n_results=2
)


print(result)