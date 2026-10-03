from pydantic import BaseModel, Field, field_validator

class Option(BaseModel):
    label: str
    text: str

class QuestionDraft(BaseModel):
    exam: str
    exam_year: int | None = None
    stage: str | None = None
    section: str | None = None
    topic: str | None = None
    subtopic: str | None = None
    question_type: str = "mcq"
    stem: str = Field(min_length=3)
    options: list[Option] = Field(default_factory=list)
    answer: str | None = None
    explanation: str | None = None
    difficulty: str | None = None
    source_page: int | None = None

    @field_validator("question_type")
    @classmethod
    def valid_type(cls, v: str) -> str:
        allowed = {"mcq", "numeric", "descriptive", "true_false"}
        if v not in allowed:
            raise ValueError(f"unsupported question_type: {v}")
        return v

class ValidationResult(BaseModel):
    valid: bool
    confidence: float = Field(ge=0, le=1)
    issues: list[str] = Field(default_factory=list)

class IngestResponse(BaseModel):
    document_id: int
    sha256: str
    pages: int
    questions_created: int
    questions_rejected: int
