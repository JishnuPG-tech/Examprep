from examprep.services.parser import parse_answer_key, parse_mcqs


def test_answer_key():
    assert parse_answer_key("Answer Key: 1-A 2-C 3-B") == {1: "A", 2: "C", 3: "B"}


def test_mcq_with_separate_key():
    text = (
        "[PAGE 1]\n"
        "1. What is 2 + 2?\n"
        "A) 3\n"
        "B) 4\n"
        "C) 5\n"
        "D) 6\n"
        "\n"
        "[PAGE 2]\n"
        "Answer Key: 1-B"
    )
    qs = parse_mcqs(text, "IBPS PO", 2026, "Quantitative Aptitude")
    assert len(qs) == 1
    assert qs[0].answer == "B"
