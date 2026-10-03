from fastapi import FastAPI, File, Form, HTTPException, UploadFile, Query
from tempfile import NamedTemporaryFile
from pathlib import Path
import json
from sqlalchemy import select
from .config import settings
from .db import init_db, SessionLocal
from .models import Question
from .services.pipeline import Pipeline

app = FastAPI(title=settings.app_name, version="0.1.0")

@app.on_event("startup")
def startup():
    init_db()

@app.get("/health")
def health():
    return {"status": "ok", "service": settings.app_name, "version": "0.1.0"}

@app.post(f"{settings.api_prefix}/documents/ingest")
async def ingest_document(file: UploadFile = File(...), exam: str = Form(...), year: int | None = Form(None), section: str | None = Form(None)):
    if file.content_type != "application/pdf":
        raise HTTPException(415, "Only PDF ingestion is enabled")
    data = await file.read()
    if len(data) > settings.max_document_mb * 1024 * 1024:
        raise HTTPException(413, "Document exceeds configured size limit")
    with NamedTemporaryFile(suffix=".pdf", delete=False) as tmp:
        tmp.write(data)
        tmp_path = tmp.name
    try:
        return Pipeline().ingest_pdf(tmp_path, exam, year, section)
    finally:
        Path(tmp_path).unlink(missing_ok=True)

@app.get(f"{settings.api_prefix}/questions")
def list_questions(
    exam: str | None = Query(None),
    section: str | None = Query(None),
    topic: str | None = Query(None),
    limit: int = Query(50, ge=1, le=200),
    offset: int = Query(0, ge=0),
):
    db = SessionLocal()
    try:
        stmt = select(Question).where(Question.validation_status == "validated")
        if exam:
            stmt = stmt.where(Question.exam == exam)
        if section:
            stmt = stmt.where(Question.section == section)
        if topic:
            stmt = stmt.where(Question.topic == topic)
        rows = db.scalars(stmt.order_by(Question.id).offset(offset).limit(limit)).all()
        return [{
            "id": q.id,
            "exam": q.exam,
            "year": q.exam_year,
            "stage": q.stage,
            "section": q.section,
            "topic": q.topic,
            "subtopic": q.subtopic,
            "type": q.question_type,
            "stem": q.stem,
            "options": json.loads(q.options_json),
            "answer": q.answer,
            "explanation": q.explanation,
            "difficulty": q.difficulty,
            "source_document_id": q.source_document_id,
            "source_page": q.source_page,
            "confidence": q.confidence,
        } for q in rows]
    finally:
        db.close()
