import chromadb

"""
chromadb or anyother vector db will be running always in the pipeline - that contains all your 
standard,polices, test stragery, plans, domain details. 

Currently since we don't have any existing db with those data- we are creating temporarily - 
only for training purpose

"""
def reterive_document(jira_user_story_description):
    client=chromadb.Client()
    collection=client.get_or_create_collection(name="coding-notes")

    collection.add(
        ids=["1","2","3","4","5"],
        documents=[
            "Recharge plans must be filtered by telecom circle",
            "expired recharge plan should not be displayed",
            "recharge plans should display validity and pricing",
            "system should handle empty plan response gracefully",
            "recharge plan should load within 3 seconds"
        ]
    )

    result=collection.query(
        query_texts=[jira_user_story_description],
        n_results=3
    )

    return result["documents"]