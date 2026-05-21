from google import genai

import json

with open("files/secret.json","r") as f:
    data=json.load(f)

client=genai.Client(api_key=data["token_gemini"])


response=client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[
        {
            "role":"system",
            "parts":[{"text":"You are a JSON generator. Give only json output. Avoid delimiters in the output"}]
        },
        {
             "role":"user",
            "parts":[{"text":"Generate json data for 5 people with different names, ages and cities"}]
        }
    ],
    config={"temperature":0.8}
    )

print(response.text)

# deserialize to json object
import json

result=json.loads(response.text)
print(result["people"][0]["name"])