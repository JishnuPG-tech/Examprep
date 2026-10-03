import re

def normalize_text(text: str) -> str:
    text = text.replace("\u00ad", "")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()

def pages(text: str) -> list[tuple[int, str]]:
    chunks = re.split(r"\[PAGE\s+(\d+)\]", text)
    result = []
    for i in range(1, len(chunks), 2):
        result.append((int(chunks[i]), chunks[i + 1].strip()))
    return result
