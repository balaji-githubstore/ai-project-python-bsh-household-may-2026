from demo4_gap_analysis.mcp_client import MCPClient
from demo4_gap_analysis import rag_utils
from demo4_gap_analysis import llm_analysis


client = MCPClient()
jira_user_story = client.run("KAN-5")
print(jira_user_story["description"])

"""
without RAG - AI reterive telecom domain standards and validation.

with RAG - 
ground the large language model (gemini, gpt, ollama) uses internal standards (proprietoryship knowledge base)
instead using some external commonly availabe standard or static data. 

"""
reterived_docs = rag_utils.reterive_document(jira_user_story["description"])
print(reterived_docs)

"""
fetch data dynamically 
use external tools (mcp/jira)
reterive context (chromadb)
reason with LLM 

produce some actional output

core building blocks of agentic AI
"""
gap_analysis_output = llm_analysis.get_gemini_llm_gap_analysis(
    "gemini-3-flash-preview", jira_user_story, reterived_docs)
print(gap_analysis_output)
print("="*50)
gap_analysis_output = llm_analysis.get_ollama_llm_gap_analyis("gemma3:1b",jira_user_story,reterived_docs)
print(gap_analysis_output)

# try sending gap_analysis_output as the comment to the same issue - KAN-5
# ollama install and then download ollama pull gemma3:1b