"""Research workflow: gather and summarize information on a topic."""

from __future__ import annotations


def summarize(topic: str, notes: list[str]) -> str:
    """Produce a short summary string from collected notes."""
    if not notes:
        return f"No notes collected for {topic}."
    joined = " ".join(n.strip() for n in notes if n.strip())
    return f"Research on {topic}: {joined}"[:500]
