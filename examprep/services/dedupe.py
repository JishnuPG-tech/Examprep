import hashlib
from rapidfuzz.fuzz import ratio
from ..schemas import QuestionDraft

def content_hash(q: QuestionDraft) -> str:
    canonical = " ".join(q.stem.lower().split()) + "|" + "|".join(" ".join(o.text.lower().split()) for o in q.options)
    return hashlib.sha256(canonical.encode()).hexdigest()

def near_duplicate(a: QuestionDraft, b: QuestionDraft, threshold: float = 96) -> bool:
    return ratio(" ".join(a.stem.lower().split()), " ".join(b.stem.lower().split())) >= threshold
