"""
pip install ollama

-- python ollama library for accessing code
"""
import ollama

response = ollama.chat(model="gemma3:1b",
                       messages=[
                           {
                               "role": "user",
                               "content": "Generate json response with name, mobilenumber"
                           }
                       ]
                       )

print(response["message"]["content"])
