from google import genai
import json

with open("files/secret.json","r") as f:
    data=json.load(f)

client=genai.Client(api_key=data["token_gemini"])

response=client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="The captial of france is paris",
    config={"temperature":0.8}
    )

print(response.text)
"""
pip install google-genai
pip install chromadb
pip install sentence-transformers   

"""
