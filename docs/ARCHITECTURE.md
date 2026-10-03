# Examprep production architecture

## Objective
Build a source-grounded banking-exam knowledge pipeline. A document is an evidence source, not merely input text.

## Processing stages
1. Intake: verify MIME/size, calculate SHA-256, record source metadata, reject duplicate source hashes.
2. Extraction: PyMuPDF for text PDFs; OCR adapter for scanned PDFs; preserve page boundaries.
3. Normalization: clean soft hyphens and whitespace while preserving page markers.
4. Segmentation: detect question blocks and answer-key blocks while retaining source pages.
5. Structuring: deterministic parser first; OpenAI-compatible model adapter for layouts that cannot be safely parsed by rules; Pydantic schema validation.
6. Validation: option cardinality, answer-key membership, required fields, confidence, provenance and review state.
7. Deduplication: exact canonical SHA-256 plus near-duplicate similarity for review.
8. Enrichment: exam, year, stage, section, topic, subtopic, difficulty and question type.
9. Persistence: PostgreSQL with linked source and question records and idempotent ingestion.
10. Serving: REST API; clients consume validated records only.

## Safety boundary
Model output is untrusted data. It is never written directly to the database. The model may extract or classify evidence, but it must not be treated as an authoritative answer source unless the source contains that answer and provenance is retained.

## Scaling path
API -> queue -> workers -> PostgreSQL/object storage. Recommended next infrastructure step: Redis or SQS-compatible queue, S3-compatible object storage, worker concurrency limits, retry/dead-letter queue, and OpenTelemetry.
