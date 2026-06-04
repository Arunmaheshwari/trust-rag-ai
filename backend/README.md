# TrustRAG AI Backend

## Overview

This backend powers the TrustRAG AI platform.

Responsibilities:

* Document Ingestion
* Embedding Generation
* Vector Search
* Agentic Workflow Execution
* Guardrail Enforcement
* Evaluation Pipelines
* API Layer

The system is built using FastAPI, LangGraph, PostgreSQL, and AWS Bedrock.

---

## Prerequisites

Install:

* Python 3.11+
* PostgreSQL 16+
* Docker Desktop
* AWS CLI
* Git
* uv Package Manager

Verify installation:

```bash
python --version
uv --version
docker --version
aws --version
```

---

## Project Structure

```text
backend/

├── agents/
├── api/
├── app/
├── data/
├── database/
├── evaluation/
├── graph/
├── ingestion/
├── logs/
├── prompts/
├── retrieval/
├── scripts/
├── tests/
├── vectorstore/

├── .env
├── pyproject.toml
├── uv.lock
└── README.md
```

---

## Create Virtual Environment

```bash
uv venv
```

Activate:

PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

---

## Install Dependencies

Install from lock file:

```bash
uv sync
```

Add package:

```bash
uv add package_name
```

Remove package:

```bash
uv remove package_name
```

Update lock file:

```bash
uv lock
```

---

## Run Application

Development mode:

```bash
uv run uvicorn main:app --reload
```

Open:

```text
http://localhost:8000
```

Swagger:

```text
http://localhost:8000/docs
```

---

## Environment Variables

Create:

```text
.env
```

Example:

```env
APP_ENV=development

AWS_REGION=us-east-1

DATABASE_URL=postgresql://postgres:password@localhost:5432/trust_rag

BEDROCK_CHAT_MODEL=
BEDROCK_EMBEDDING_MODEL=

LOG_LEVEL=INFO
```

Never commit:

```text
.env
```

to Git.

---

## Database Setup

### Create Database

Open PostgreSQL:

```sql
CREATE DATABASE trust_rag;
```

Connect:

```sql
\c trust_rag
```

Enable pgvector:

```sql
CREATE EXTENSION IF NOT EXISTS vector;
```

Verify:

```sql
SELECT * FROM pg_extension;
```

---

## AWS Setup

Configure credentials:

```bash
aws configure
```

Provide:

```text
AWS Access Key
AWS Secret Key
AWS Region
```

Verify:

```bash
aws sts get-caller-identity
```

Expected:

```json
{
  "UserId": "...",
  "Account": "...",
  "Arn": "..."
}
```

---

## Bedrock Models

Recommended:

### Generation

Claude Sonnet

### Critique

Claude Haiku

### Embeddings

Titan Text Embeddings

Configuration will be stored in:

```text
app/config/settings.py
```

---

## Testing

Run all tests:

```bash
pytest
```

Coverage:

```bash
pytest --cov
```

---

## Formatting

Format code:

```bash
ruff format .
```

Lint:

```bash
ruff check .
```

---

## Current Development Phase

Phase 1

Self-Correcting RAG using LangGraph

Upcoming:

* Retriever Agent
* Generator Agent
* Critic Agent
* Query Rewriter Agent
* Vector Search Pipeline
