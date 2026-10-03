from datetime import datetime
from sqlalchemy import DateTime, Float, Integer, String, Text, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column
from .db import Base

class SourceDocument(Base):
    __tablename__ = "source_documents"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    sha256: Mapped[str] = mapped_column(String(64), unique=True, index=True)
    filename: Mapped[str] = mapped_column(String(512))
    mime_type: Mapped[str] = mapped_column(String(128))
    source_url: Mapped[str | None] = mapped_column(String(2048))
    rights_status: Mapped[str] = mapped_column(String(64), default="unknown")
    page_count: Mapped[int] = mapped_column(Integer, default=0)
    extracted_text: Mapped[str] = mapped_column(Text, default="")
    extraction_method: Mapped[str] = mapped_column(String(64), default="text")
    processing_version: Mapped[str] = mapped_column(String(32), default="0.1.0")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

class Question(Base):
    __tablename__ = "questions"
    __table_args__ = (UniqueConstraint("content_hash", name="uq_question_content_hash"),)
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    source_document_id: Mapped[int] = mapped_column(Integer, index=True)
    source_page: Mapped[int | None] = mapped_column(Integer)
    exam: Mapped[str] = mapped_column(String(64), index=True)
    exam_year: Mapped[int | None] = mapped_column(Integer, index=True)
    stage: Mapped[str | None] = mapped_column(String(32))
    section: Mapped[str | None] = mapped_column(String(64), index=True)
    topic: Mapped[str | None] = mapped_column(String(128), index=True)
    subtopic: Mapped[str | None] = mapped_column(String(128))
    question_type: Mapped[str] = mapped_column(String(32), default="mcq")
    stem: Mapped[str] = mapped_column(Text)
    options_json: Mapped[str] = mapped_column(Text, default="[]")
    answer: Mapped[str | None] = mapped_column(Text)
    explanation: Mapped[str | None] = mapped_column(Text)
    difficulty: Mapped[str | None] = mapped_column(String(32))
    content_hash: Mapped[str] = mapped_column(String(64), index=True)
    validation_status: Mapped[str] = mapped_column(String(32), default="pending")
    confidence: Mapped[float] = mapped_column(Float, default=0.0)
    review_status: Mapped[str] = mapped_column(String(32), default="unreviewed")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
