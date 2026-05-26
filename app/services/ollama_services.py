import os
from langchain_ollama import OllamaLLM

MODEL_NAME = os.getenv("MODEL_NAME")
llm = OllamaLLM(model=MODEL_NAME)

# print(MODEL_NAME)
