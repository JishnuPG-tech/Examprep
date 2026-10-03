import json
import re
from .normalizer import pages
from ..schemas import Option, QuestionDraft

OPTION_RE = re.compile(r"^\s*([A-Ea-e])\s*[\).:-]\s*(.+?)\s*$")
QUESTION_RE = re.compile(r"(?m)^\s*(\d{1,3})[.)]\s+(.+?)(?=^\s*\d{1,3}[.)]\s+|\Z)", re.S)

def parse_mcqs(text: str, exam: str, year: int | None = None, section: str | None = None) -> list[QuestionDraft]:
    out = []
    for page_no, page_text in pages(text):
        for match in QUESTION_RE.finditer(page_text):
            block = match.group(2).strip()
            lines = [x.strip() for x in block.splitlines() if x.strip()]
            options = []
            stem_lines = []
            for line in lines:
                m = OPTION_RE.match(line)
                if m:
                    options.append(Option(label=m.group(1).upper(), text=m.group(2).strip()))
                else:
                    stem_lines.append(line)
            if len(options) >= 2 and stem_lines:
                out.append(QuestionDraft(exam=exam, exam_year=year, section=section, stem=" ".join(stem_lines), options=options, source_page=page_no))
    return out

def parse_json_questions(payload: str, exam: str) -> list[QuestionDraft]:
    data = json.loads(payload)
    if isinstance(data, dict): data = data.get("questions", [])
    return [QuestionDraft.model_validate({**q, "exam": q.get("exam", exam)}) for q in data]
