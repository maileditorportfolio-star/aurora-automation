from aurora_automation.workflows.data_entry import ExtractionError, extract
from aurora_automation.workflows.email_triage import Email, Priority, classify, route
from aurora_automation.workflows.research import summarize


def test_email_triage_high_priority():
    email = Email("a@b.com", "Urgent invoice", "Please pay asap")
    assert classify(email) == Priority.HIGH
    assert route(email) == "queue:high"


def test_email_triage_low_priority():
    email = Email("a@b.com", "Hello", "hi")
    assert classify(email) == Priority.LOW


def test_email_triage_body_boundary():
    short = Email("a@b.com", "Hello", "x" * 500)
    assert classify(short) == Priority.LOW
    long = Email("a@b.com", "Hello", "x" * 501)
    assert classify(long) == Priority.NORMAL


def test_email_triage_invalid_sender():
    email = Email("not-an-email", "Hello", "hi")
    try:
        classify(email)
    except ValueError:
        return
    raise AssertionError("expected ValueError")


def test_data_entry_extract():
    rec = extract("Contact John Doe at john@example.com or +1 555-123-4567")
    assert rec.email == "john@example.com"
    assert rec.name == "John Doe"
    assert rec.phone is not None


def test_data_entry_no_contact_raises():
    try:
        extract("nothing useful here 123")
    except ExtractionError:
        return
    raise AssertionError("expected ExtractionError")


def test_data_entry_no_email_or_phone():
    rec = extract("Contact Jane Roe")
    assert rec.email is None
    assert rec.phone is None
    assert rec.name == "Jane Roe"


def test_research_summarize():
    out = summarize("AI", ["note one", "note two"])
    assert "AI" in out
    assert "note one" in out


def test_research_empty():
    assert summarize("AI", []) == "No notes collected for AI."
