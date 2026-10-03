from examprep.schemas import Option, QuestionDraft
from examprep.services.validator import validate_question


def test_valid_mcq():
    q = QuestionDraft(
        exam="IBPS PO",
        stem="What is 2 + 2?",
        options=[
            Option(label="A", text="3"),
            Option(label="B", text="4"),
            Option(label="C", text="5"),
            Option(label="D", text="6"),
        ],
        answer="B",
    )
    r = validate_question(q)
    assert r.valid and r.confidence == 1


def test_invalid_answer():
    q = QuestionDraft(
        exam="IBPS PO",
        stem="What is 2 + 2?",
        options=[
            Option(label="A", text="3"),
            Option(label="B", text="4"),
            Option(label="C", text="5"),
            Option(label="D", text="6"),
        ],
        answer="E",
    )
    r = validate_question(q)
    assert not r.valid
