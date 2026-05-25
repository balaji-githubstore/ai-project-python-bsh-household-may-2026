"""
Langchain - orchestration of LLM apps 

LLMS (OLLAMA/Open AI/ Claude)
Vector DB (FAISS, Chromadb)
Tools, RAG pipeline, Agents 
"""

from langchain_chroma import Chroma
from langchain_ollama import OllamaLLM, OllamaEmbeddings

from github_package import pr_fetcher
from jira_package.jira_mcp import MCPClient


embeddings = OllamaEmbeddings(model="nomic-embed-text:latest")
db = Chroma(persist_directory="rag/vector_db", embedding_function=embeddings)
retriever = db.as_retriever(search_kwargs={"k": 5})

# load pr code changes
pr_changes = pr_fetcher.load_pr_code("balaji-githubstore/java-hybrid-framework-playwright-kpmg-jan-2026",4)

# retrieve policies
docs = retriever.invoke(pr_changes)
coding_policies = ("\n".join([doc.page_content for doc in docs]))

client = MCPClient()
ticket_content = client.get_jira_ticket_content("KAN-5")


prompt = f"""
You are a principal engineer reviewing the PR

Validate Both:
1. Does PR satisfy jira requirment?
2. Does the PR follow coding policies? 

JIRA REQUIREMENT: {ticket_content}
CODING POLICY: {coding_policies}
PR CODE: {pr_changes}

Output Clearly: 
    - Missing requirement
    - Policy violations 
    - Security Issues 
    - Suggested Improvements 

"""

llm = OllamaLLM(model="gemma3:1b")
response = llm.invoke(prompt)
print(response)
