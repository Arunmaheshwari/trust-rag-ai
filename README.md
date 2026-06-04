# TrustRAG AI

## Overview

TrustRAG AI is a production-grade Agentic AI platform designed to build trustworthy Retrieval-Augmented Generation (RAG) systems.

Unlike traditional RAG pipelines that simply retrieve information and generate answers, TrustRAG AI introduces self-correction, guardrails, and automated evaluation to improve reliability and reduce hallucinations.

The platform combines:

* Self-Correcting RAG using LangGraph
* Hallucination Detection and Critique Agents
* Prompt Injection and PII Protection
* Automated LLM Evaluation Pipelines
* AWS Bedrock Integration
* Production Monitoring and Observability

---

## Why TrustRAG AI Exists

Most RAG systems follow a simple workflow:

User Question → Retrieve Documents → Generate Answer

This approach often fails because:

* Retrieved documents may not contain enough information.
* LLMs can hallucinate.
* Answers may not be grounded in retrieved context.
* Prompt injection attacks can bypass instructions.
* Teams lack automated evaluation and regression testing.

TrustRAG AI addresses these challenges through agentic workflows, safety guardrails, and continuous evaluation.

---

## Key Features

### Self-Correcting RAG

* Multi-step retrieval
* Query rewriting
* Critique and validation
* Retry mechanism
* Grounded answer generation

### Agentic Workflow

Built using LangGraph with cyclical state transitions.

* Retriever Agent
* Generator Agent
* Critic Agent
* Query Rewriter Agent

### LLM Guardrails

Input Protection:

* Prompt Injection Detection
* Jailbreak Detection
* PII Detection

Output Protection:

* Toxicity Detection
* JSON Schema Validation
* Source Citation Enforcement

### Automated Evaluation

Continuous testing against a golden dataset.

Metrics:

* Hallucination Rate
* Faithfulness
* Answer Relevancy
* Latency
* Cost Per Query

### Production Ready

* FastAPI APIs
* PostgreSQL + pgvector
* Docker
* AWS Bedrock
* GitHub Actions
* Monitoring and Logging

---

## High-Level Architecture

```text
User Query
    │
    ▼
Input Guardrails
    │
    ▼
Retriever Agent
    │
    ▼
Generator Agent
    │
    ▼
Critic Agent
    │
 ┌──┴──┐
 │Pass │
 └──┬──┘
    │
    ▼
Output Guardrails
    │
    ▼
 Final Answer

Critic Reject
      │
      ▼
Query Rewriter
      │
      ▼
Re-Retrieve
      │
      └───> Generator
```

---

## Project Structure

```text
trust-rag-ai/

├── backend/
├── frontend/
├── deployment/
├── docs/

├── README.md
└── .gitignore
```

---

## Technology Stack

### Backend

* Python 3.11
* FastAPI
* LangGraph
* LangChain
* AWS Bedrock

### Database

* PostgreSQL
* pgvector

### Evaluation

* Ragas
* DeepEval
* LangSmith

### Frontend

* Next.js
* React
* TypeScript

### Deployment

* Docker
* AWS ECS/Fargate
* GitHub Actions

---

## Screenshots

Screenshots and demos will be added during implementation.

---

## Quick Start

Clone the repository:

```bash
git clone <repository-url>
cd trust-rag-ai
```

Backend setup:

```bash
cd backend

uv venv
uv sync
```

Run backend:

```bash
uv run uvicorn main:app --reload
```

Frontend setup:

```bash
cd frontend

npm install
npm run dev
```

---

## Development Roadmap

### Phase 1

Self-Correcting RAG

### Phase 2

Guardrails Gateway

### Phase 3

Automated Evaluation Framework

### Phase 4

Production Deployment and Monitoring

---

## License

MIT License
