import chromadb

client=chromadb.Client()

collection=client.get_or_create_collection(name="coding-notes")

"""
Add document to the chromadb collection 
Store 3 text documents 
Store raw text and then convert text into embedding 
"""
collection.add(
    ids=["1","2","3"],
    documents=[
        "python is used for AI and automation",
        "Playwright is used for browser testing",
        "docker is used for containerization"
    ]
)

result=collection.query(
    query_texts=["tools for web testing"],
    n_results=2
)


print(result)