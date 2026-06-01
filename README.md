# Agentic AI E2E Project

## Overview
This repository demonstrates an end-to-end, agentic AI workflow for automating common engineering tasks (Jira analysis, PR review, test-case generation, RAG retrieval, and test script generation). It stitches together lightweight agents, service wrappers, and a RAG vector store to enable experiments and small production proofs-of-concept.

## Key Concepts
- Agents: modular Python components implementing specific capabilities (e.g., `jira_analyze_agent.py`, `pr_review_agent.py`).
- RAG (Retrieval-Augmented Generation): vectorized documents stored in a Chroma DB under `data/vector_db/` and used by the `rag` helpers to retrieve context.
- Services: thin wrappers around external systems (GitHub, Jira, Ollama) in `app/services/`.
- Workflows: orchestration logic for composing agents and services in `workflows/`.

## Repository Structure

- `main.py` — project entrypoint (example runner)
- `app/agents/` — agents that perform domain tasks:
	- `jira_analyze_agent.py` — analyzes Jira issues and produces summaries or recommended actions
	- `pr_review_agent.py` — inspects PRs and generates reviews/comments
	- `rag_agent.py` — coordinates retrieval from the vector DB and generation
	- `testcase_agent.py` — creates test case ideas from inputs
	- `testscript_agent.py` — generates test scripts from test cases
- `app/services/` — external integrations and utilities:
	- `github_services.py` — GitHub API helpers
	- `jira_services.py` — Jira API helpers
	- `ollama_services.py` — local LLM service helper
	- `prompt_loader.py` — loads prompts/templates used by agents
- `data/`:
	- `policies/` — company policies used for safety or constraints
	- `testcases/` — example test-case CSVs
	- `vector_db/` — Chroma DB files and persisted vectors
- `rag/` — tooling to build and query the vector DB (`build_vector_db.py`, `retriever.py`)
- `workflows/` — higher-level orchestration (e.g., `langgraph_workflow.py`)

## Setup

Prerequisites:
- Python 3.10+ virtual environment
- Project dependencies listed in `requirements.txt`

Quickstart:

1. Create and activate a virtual environment:
2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Populate your environment variables or `.env` (GitHub token, Jira creds, Ollama URL) as required by `app/services/*`.
JIRA_URL=https://dbalacloud.atlassian.net/
JIRA_EMAIL=
JIRA_TOKEN=
MODEL_NAME=gemma3:1b
GITHUB_TOKEN=

4. (Optional) Build or update the RAG vector DB:

```powershell
python rag/build_vector_db.py
```

5. Run the example runner:

```powershell
python main.py
```

## How it Works (End-to-End)

1. Input (issue, PR, or prompt) is provided to a workflow (for example, `workflows/langgraph_workflow.py`).
2. The workflow calls one or more agents in `app/agents/`.
3. Agents consult `app/services/*` to fetch external data (issues, PR diffs, policy docs).
4. If context is needed, agents call the `rag` retriever to fetch relevant documents from `data/vector_db/`.
5. Agents craft prompts (via `prompt_loader.py`) and call the configured LLM (via `ollama_services.py` or other service wrappers).
6. Outputs are returned to the workflow which may post comments (GitHub), update Jira, or write artifacts (test cases/scripts) locally.

## Running Common Tasks

- Run the Jira analysis agent in isolation:

```powershell
python -c "from app.agents.jira_analyze_agent import JiraAnalyzeAgent; JiraAnalyzeAgent().run()"
```

- Run the PR review agent:

```powershell
python -c "from app.agents.pr_review_agent import PRReviewAgent; PRReviewAgent().run()"
```

Adjust calls/arguments according to each agent's CLI or function signatures.

## Development Notes
- Add new agents to `app/agents/` and wire any external calls through `app/services/`.
- Keep prompts in `app/services/prompt_loader.py` to centralize templates.
- When updating the RAG DB, commit only the metadata and not the large vector blob.

## Troubleshooting
- If external APIs fail, ensure tokens and endpoints are set and network access is available.
- If the RAG retriever returns poor results, re-run `rag/build_vector_db.py` after improving document preprocessing.

## Next Steps for Contributors
- Add README examples showing common CLI args for each agent.
- Add automated tests for agent logic.
- Add a small Dockerfile to containerize the runner and Ollama dependency.

## License & Contact
Project is internal — follow company guidelines for sharing. For questions, contact the repository owner.

