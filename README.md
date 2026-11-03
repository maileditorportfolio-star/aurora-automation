# Aurora Automation

AI agents and automation workflows that replace manual tasks — email triage, data entry, and research — built with Python.

This repository contains **source code only**. No credentials or runtime data are committed — create your own environment from the provided `.env.example`.

## Requirements

- Python 3.10+
- (Optional) An API key for the LLM provider you choose

## Setup

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

pip install -e ".[dev]"
cp .env.example .env   # edit with your values
```

## Available commands

| Command | What it does |
| --- | --- |
| `pytest` | Run the test suite |
| `ruff check .` | Lint |
| `ruff format .` | Format |
| `mypy src` | Type check |
| `aurora --help` | CLI entry point |

## Workflows

- `email_triage` — classify and route incoming emails
- `data_entry` — extract structured data from unstructured input
- `research` — gather and summarize information on a topic

## Verification

```bash
pip install -e ".[dev]"
pytest
ruff check .
ruff format --check .
mypy src
```

## License

Released for use and modification.