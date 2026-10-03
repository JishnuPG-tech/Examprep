import json
from pathlib import Path
from sqlalchemy import select
from ..config import settings
from ..db import SessionLocal
from ..models import Question, SourceDocument
from ..schemas import QuestionDraft
from .dedupe import content_hash
from .extractor import extract_pdf
from .normalizer import normalize_text
from .parser import parse_mcqs
from .validator import validate_question

class Pipeline:
    def ingest_pdf(self, path: str, exam: str, year: int | None = None, section: str | None = None) -> dict:
        extracted = extract_pdf(path)
        text = normalize_text(extracted.text)
        db = SessionLocal()
        try:
            existing = db.scalar(select(SourceDocument).where(SourceDocument.sha256 == extracted.sha256))
            if existing:
                return {"document_id": existing.id, "sha256": existing.sha256, "pages": existing.page_count, "questions_created": 0, "questions_rejected": 0, "idempotent": True}
            doc = SourceDocument(sha256=extracted.sha256, filename=extracted.filename, mime_type=extracted.mime_type, page_count=extracted.pages, extracted_text=text, extraction_method=extracted.method)
            db.add(doc); db.flush()
            created = rejected = 0
            drafts = parse_mcqs(text, exam, year, section)
            for draft in drafts:
                result = validate_question(draft)
                if not result.valid or result.confidence < settings.publish_min_confidence:
                    rejected += 1
                    continue
                h = content_hash(draft)
                if db.scalar(select(Question).where(Question.content_hash == h)):
                    continue
                q = Question(source_document_id=doc.id, source_page=draft.source_page, exam=draft.exam, exam_year=draft.exam_year, stage=draft.stage, section=draft.section, topic=draft.topic, subtopic=draft.subtopic, question_type=draft.question_type, stem=draft.stem, options_json=json.dumps([o.model_dump() for o in draft.options]), answer=draft.answer, explanation=draft.explanation, difficulty=draft.difficulty, content_hash=h, validation_status="validated", confidence=result.confidence)
                db.add(q); created += 1
            db.commit()
            return {"document_id": doc.id, "sha256": extracted.sha256, "pages": extracted.pages, "questions_created": created, "questions_rejected": rejected, "idempotent": False}
        except Exception:
            db.rollback(); raise
        finally:
            db.close()
