import json
import re
from .normalizer import pages
from ..schemas import Option, QuestionDraft

OPTION_RE = re.compile(r"^\s*([A-Ea-e])\s*[\).:-]\s*(.+?)\s*$")
QUESTION_RE = re.compile(r"(?m)^\s*(\d{1,3})[.)]\s+(.+?)(?=^\s*\d{1,3}[.)]\s+|\Z)", re.S)
ANSWER_RE = re.compile(r"(?i)\b(\d{1,3})\s*[-.):]?\s*([A-E])\b")

def parse_answer_key(text: str) -> dict[int, str]:
    result: dict[int, str] = {}
    for line in text.splitlines():
        if not re.search(r"(?i)answer|key|correct", line):
            continue
        for number, label in ANSWER_RE.findall(line):
            result[int(number)] = label.upper()
    return result

def parse_mcqs(text: str, exam: str, year: int | None = None, section: str | None = None) -> list[QuestionDraft]:
    answer_key = parse_answer_key(text)
    out = []
    for page_no, page_text in pages(text):
        for match in QUESTION_RE.finditer(page_text):
            number = int(match.group(1))
            block = match.group(2).strip()
            lines = [x.strip() for x in block.splitlines() if x.strip()]
            options = []
            stem_lines = []
            for line in lines:
                m = OPTION_RE.match(line)
                if m:
                    options.append(Option(label=m.group(1).upper(), text=m.group(2).strip()))
                elif not re.search(r"(?i)^(answer|answer key|solutions?)\b", line):
                    stem_lines.append(line)
            if len(options) >= 2 and stem_lines:
                answer = answer_key.get(number)
                out.append(QuestionDraft(exam=exam, exam_year=year, section=section, stem=" ".join(stem_lines), options=options, answer=answer, source_page=page_no))
    return out

def parse_json_questions(payload: str, exam: str) -> list[QuestionDraft]:
    data = json.loads(payload)
    if isinstance(data, dict):
        data = data.get("questions", [])
    return [QuestionDraft.model_validate({**q, "exam": q.get("exam", exam)}) for q in data]
