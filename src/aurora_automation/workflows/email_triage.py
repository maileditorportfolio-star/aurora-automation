"""Email triage workflow: classify and route incoming emails."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from pydantic import BaseModel, EmailStr, ValidationError


class Priority(str, Enum):
    HIGH = "high"
    NORMAL = "normal"
    LOW = "low"


@dataclass
class Email:
    sender: str
    subject: str
    body: str


class EmailModel(BaseModel):
    sender: EmailStr
    subject: str
    body: str


def validate_email(email: Email) -> EmailModel:
    """Validate an Email using pydantic, raising ValueError on failure."""
    try:
        return EmailModel(sender=email.sender, subject=email.subject, body=email.body)
    except ValidationError as exc:
        raise ValueError(str(exc)) from exc


def classify(email: Email) -> Priority:
    """Classify an email into a priority level."""
    validate_email(email)
    text = f"{email.subject} {email.body}".lower()
    urgent_keywords = ("urgent", "asap", "invoice", "payment", "down", "outage")
    if any(k in text for k in urgent_keywords):
        return Priority.HIGH
    if len(email.body) > 500:
        return Priority.NORMAL
    return Priority.LOW


def route(email: Email) -> str:
    """Return the mailbox/queue an email should be routed to."""
    priority = classify(email)
    return f"queue:{priority.value}"
