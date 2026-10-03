from dataclasses import dataclass
from pathlib import Path
import hashlib
import fitz

@dataclass
class ExtractedDocument:
    sha256: str
    filename: str
    mime_type: str
    pages: int
    text: str
    method: str

def extract_pdf(path: str | Path) -> ExtractedDocument:
    p = Path(path)
    raw = p.read_bytes()
    doc = fitz.open(stream=raw, filetype="pdf")
    pages = []
    for i, page in enumerate(doc, start=1):
        text = page.get_text("text") or ""
        pages.append(f"\n[PAGE {i}]\n{text.strip()}")
    return ExtractedDocument(hashlib.sha256(raw).hexdigest(), p.name, "application/pdf", len(doc), "\n".join(pages), "pymupdf")
