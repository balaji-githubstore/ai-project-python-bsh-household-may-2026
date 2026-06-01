# PR Review Project

This repository contains tools and components for automating and assisting with pull request reviews. It includes utilities to fetch and analyze PRs, integrate with issue trackers, run review engines, and perform retrieval-augmented generation for reviewer assistance. The project is organized into small packages focusing on specific responsibilities:

- `github_package/` — utilities for fetching and processing pull requests from GitHub.
- `jira_package/` — integration helpers for Jira and related MCP workflows.
- `reviewer_package/` — core review engine logic used to evaluate and summarize PR changes.
- `rag/` — retrieval-augmented generation helpers and embedding utilities.
- `vector_db/` — local vector store and database artifacts used for semantic search.
- `files/` — supportive files and secrets used by scripts (kept out of source control where appropriate).

The codebase is intended for experimentation and building automation around code review workflows, combining automation (fetchers, parsers) with ML-powered assistance (embeddings, semantic search, review heuristics).

For more details about specific modules, see the package subdirectories.
