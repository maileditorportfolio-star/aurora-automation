"""Data entry workflow: extract structured records from unstructured text."""

from __future__ import annotations

import re
from dataclasses import dataclass


@dataclass
class Record:
    name: str | None = None
    email: str | None = None
    phone: str | None = None


_EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
_PHONE_RE = re.compile(r"\+?\d[\d\s\-()]{7,}\d")


class ExtractionError(ValueError):
    """Raised when no contact information can be extracted."""


def extract(text: str) -> Record:
    """Extract name/email/phone from free-form text."""
    record = Record()
    emails = _EMAIL_RE.findall(text)
    if emails:
        record.email = emails[0]
    phones = _PHONE_RE.findall(text)
    if phones:
        record.phone = phones[0].strip()
    # naive name: first capitalized two-word sequence, skipping common lead words
    cleaned = re.sub(r"\b(Contact|Email|Phone|Name)\b", "", text)
    name_match = re.search(r"\b([A-Z][a-z]+ [A-Z][a-z]+)\b", cleaned)
    if name_match:
        record.name = name_match.group(1)
    if record.email is None and record.phone is None and record.name is None:
        raise ExtractionError("no contact information found")
    return record
