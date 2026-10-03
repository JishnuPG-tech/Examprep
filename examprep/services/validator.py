import re
from ..schemas import QuestionDraft, ValidationResult

def validate_question(q: QuestionDraft) -> ValidationResult:
    issues = []
    if q.question_type == "mcq":
        labels = [o.label for o in q.options]
        if len(labels) < 4: issues.append("MCQ must contain at least four options")
        if len(set(labels)) != len(labels): issues.append("Duplicate option labels")
        if q.answer and q.answer.upper() not in {x.upper() for x in labels}: issues.append("Answer key is not an option label")
    if len(q.stem.split()) < 3: issues.append("Question stem is too short")
    if q.answer is None: issues.append("Missing answer key")
    confidence = max(0.0, 1.0 - 0.2 * len(issues))
    return ValidationResult(valid=not issues, confidence=confidence, issues=issues)
