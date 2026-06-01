# Python AI Project — BSH Household AI

Short description

- **Purpose:** A collection of demos, utilities, and experiments for applying large language models, vector databases, and Model Control Plane (MCP) tooling to household appliance use-cases and developer workflows.
- **Scope:** Examples showing integration with Gemini, Ollama, ChromaDB, and automated MCP interactions (Jira, task automation). This repository is intended for prototyping and learning rather than production deployment.

Project structure

- `automation_scripts/` — automation and orchestration scripts (KAN-8.py, KAN-9.py).
- `db/` — local database and indexing artifacts (includes Chroma/SQLite stores).
- `demo1_google_llm_package/` — demo code using Google/Gemini LLMs.
- `demo2_vectoization_package/` — examples for sentence vectors and ChromaDB usage.
- `demo3_mcp/` — demo scripts for MCP integration and asynchronous examples.
- `demo4_gap_analysis/` — tools for gap analysis, RAG utilities, and runner scripts.
- `demo5_ollama_package/` — Ollama LLM demo.
- `demo6_advance_mcp_draft_package/` — advanced MCP Jira search drafts.
- `files/` — sample data and secrets (sensitive files should not be committed to public repos).
- `requirements.txt` — Python dependencies for the demos.

Getting started

1. Create and activate a Python virtual environment.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. Review demo folders and run a demo script. Many demos require API keys or local services (Gemini/Google keys, Ollama server, ChromaDB). Set required credentials in `files/secret.json` or environment variables as appropriate.

Notes and recommendations

- This repository is for experimentation: validate credentials and sanitize secrets before sharing.
- Use the `demo2_vectoization_package` and `db/` folders as starting points for retrieval-augmented generation (RAG) prototypes.
- For MCP/Jira demos, configure your Jira credentials and endpoints before running the scripts.

Contact / Next steps

If you want, I can:
- run tests or a selected demo to verify environment setup,
- add a CONTRIBUTING section or examples for one demo,
- or create a secure `.env` example for required credentials.

