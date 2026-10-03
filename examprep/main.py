from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from tempfile import NamedTemporaryFile
from pathlib import Path
from .config import settings
from .db import init_db
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
        raise HTTPException(415, "Only PDF ingestion is enabled in this first production pipeline")
    data = await file.read()
    if len(data) > settings.max_document_mb * 1024 * 1024:
        raise HTTPException(413, "Document exceeds configured size limit")
    with NamedTemporaryFile(suffix=".pdf", delete=False) as tmp:
        tmp.write(data); tmp_path = tmp.name
    try:
        return Pipeline().ingest_pdf(tmp_path, exam, year, section)
    finally:
        Path(tmp_path).unlink(missing_ok=True)
