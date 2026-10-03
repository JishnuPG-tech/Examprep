# Examprep — Banking Exam Knowledge & Question Pipeline

Production-oriented pipeline for turning legally obtained banking-exam documents into a validated, provenance-preserving question bank.

## Scope

Initial domain coverage: IBPS PO/MT, IBPS RRB Officer Scale I / Office Assistant, SBI PO / Junior Associate, and RBI Assistant. The taxonomy is versioned because exam patterns and notifications change.

## Pipeline

Document -> Ingest -> Extract -> Normalize -> Segment -> Classify -> Extract Questions -> Validate -> Deduplicate -> Enrich -> Persist -> API

Every question retains source document, source page/location, extraction method, source hash, processing version, validation status, confidence, and review status.

## Production principles

- Never silently invent an answer.
- Preserve source provenance.
- Separate deterministic parsing from model-assisted extraction.
- Validate structured model output before persistence.
- Make processing idempotent using content hashes.
- Keep taxonomy/version metadata with every question.
- Quarantine low-confidence records instead of publishing them.
- Support human review.
- Operators are responsible for lawful use of source material.

## Stack

Python 3.12, FastAPI, Pydantic v2, SQLAlchemy, PostgreSQL, PyMuPDF, optional OCR adapter, OpenAI-compatible LLM adapter, pytest, Docker.

## Run

Copy .env.example to .env, then run docker compose up --build. API is on port 8000 and OpenAPI is at /docs.

CLI: python -m examprep.cli ingest ./data/sample.pdf

## Quality gate

A record is publishable only when required fields and provenance exist, structural validation passes, duplicate checks pass, and validation confidence meets the configured threshold. Low-confidence records are retained for review.
