# Aurora Automation

[![CI](https://github.com/maileditorportfolio-star/aurora-automation/actions/workflows/ci.yml/badge.svg)](https://github.com/maileditorportfolio-star/aurora-automation/actions/workflows/ci.yml)

AI agents and automation workflows that replace manual tasks — **email triage**, **data entry**, and **research** — built with Python. Workflows are small, typed, and tested, with a CLI entry point and a configured CI pipeline.

This repository contains **source code only**. No credentials or runtime data are committed — create your own environment from the provided `.env.example`.

---

## Table of contents

1. [Features](#features)
2. [Tech stack](#tech-stack)
3. [Requirements](#requirements)
4. [Download the project](#download-the-project)
5. [Local setup](#local-setup)
6. [Project structure](#project-structure)
7. [Available commands](#available-commands)
8. [Testing](#testing)
9. [Verification](#verification)
10. [Customizing the project](#customizing-the-project)
11. [CLI reference](#cli-reference)
12. [Docker](#docker)
13. [Troubleshooting](#troubleshooting)
14. [Security](#security)
15. [License](#license)

---

## Features

### Workflows
- **Email triage** (`email_triage`) — classify incoming emails into priority levels (`high` / `normal` / `low`) and route them to a queue, with Pydantic-validated input.
- **Data entry** (`data_entry`) — extract structured records (name, email, phone) from free-form text, raising `ExtractionError` when nothing is found.
- **Research** (`research`) — gather notes and produce a concise summary for a topic.

### Quality & tooling
- **Typed code** — strict mypy across `src/`, dataclasses and enums for models.
- **Linted & formatted** — ruff (lint + format) at 100 columns.
- **Tested** — pytest with coverage, 98%+ on the source, enforced threshold in CI.
- **Reproducible installs** — pinned `requirements.txt` lockfile generated with pip-compile.
- **CI/CD** — GitHub Actions runs lint, format, type check, dependency audit, and tests on every push/PR.
- **Docker** — container image builds from a slim Python base.

---

## Tech stack

| Layer | Technology |
| --- | --- |
| Language | Python 3.10+ (developed on 3.12) |
| CLI | Typer |
| Validation | Pydantic (with email support) |
| HTTP client | httpx |
| Config | python-dotenv |
| Testing | pytest, pytest-cov |
| Lint/format | ruff |
| Type checking | mypy (strict) |

Dependencies are declared in `pyproject.toml` and pinned in `requirements.txt`.

---

## Requirements

- **Python 3.10+** (developed on 3.12)
- **pip 23+**

Check your version:

```bash
python --version
pip --version
```

---

## Download the project

### Option A — clone with Git (recommended)

```bash
git clone https://github.com/maileditorportfolio-star/aurora-automation.git
cd aurora-automation
```

Already have it locally but want the latest? Inside the project folder:

```bash
git pull origin main
pip install -r requirements.txt
```

### Option B — download as a ZIP

1. Open the repository on GitHub: <https://github.com/maileditorportfolio-star/aurora-automation>
2. Click **Code → Download ZIP**
3. Unzip it and rename the folder to `aurora-automation`
4. Open a terminal inside that folder

---

## Local setup

### 1. Create and activate a virtual environment

```bash
python -m venv .venv

# Windows PowerShell
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
pip install -e ".[dev]"
```

### 3. Configure environment variables

```bash
cp .env.example .env   # Windows: Copy-Item .env.example .env
```

Edit `.env`:

```ini
LLM_PROVIDER=openai
LLM_API_KEY=
LLM_MODEL=gpt-4o-mini
LOG_LEVEL=info
```

> `.env` is git-ignored — your secrets never leave your machine.

### 4. Run the tests

```bash
pytest
```

### 5. Run the CLI

```bash
aurora
```

---

## Project structure

```
aurora-automation/
├── .github/
│   ├── workflows/              # ci.yml
│   ├── pull_request_template.md
│   └── dependabot.yml          # weekly pip updates
├── src/
│   └── aurora_automation/
│       ├── __init__.py         # package version
│       ├── cli.py              # Typer CLI entry point
│       └── workflows/
│           ├── __init__.py
│           ├── email_triage.py # classify + route emails
│           ├── data_entry.py   # extract structured records
│           └── research.py     # summarize notes
├── tests/
│   ├── test_workflows.py       # workflow specs
│   └── test_cli.py             # CLI specs
├── docs/
│   └── verification.md         # reproducible verification steps
├── Dockerfile
├── pyproject.toml              # project + tool config
├── requirements.txt            # pinned lockfile
├── .env.example
├── .gitignore
├── .gitattributes
├── AGENTS.md                   # agent-facing project memory
├── CHANGELOG.md
├── CONTRIBUTING.md
├── README.md
└── LICENSE (none yet)
```

---

## Available commands

Run from the repository root.

| Command | What it does |
| --- | --- |
| `pytest` | Run the test suite (with coverage) |
| `ruff check .` | Lint |
| `ruff format .` | Format |
| `ruff format --check .` | Check formatting |
| `mypy src` | Type check |
| `aurora` | CLI entry point (prints version) |
| `pip-audit` | Dependency vulnerability scan |

---

## Testing

The repository ships with a pytest suite covering all three workflows plus the CLI.

```bash
pytest                       # all specs, coverage enforced at 80%
pytest tests/test_cli.py     # CLI specs only
```

Coverage is enforced: the source must stay at or above **80%**. `pytest` fails the build when the threshold regresses.

---

## Verification

Everything below is reproducible from a fresh clone. [`docs/verification.md`](docs/verification.md) records the exact commands.

```bash
python -m venv .venv
.venv\Scripts\activate          # or: source .venv/bin/activate
pip install -r requirements.txt
pip install -e ".[dev]"
pytest
ruff check .
ruff format --check .
mypy src
```

---

## Customizing the project

### Add a new workflow
1. Create `src/aurora_automation/workflows/<name>.py` with typed functions.
2. Export it from `src/aurora_automation/workflows/__init__.py`.
3. Add a spec in `tests/test_workflows.py` pinning the new behavior.
4. Run `pytest` and commit the feature + test together.

### Change validation rules
- Email validation lives in `email_triage.validate_email` (Pydantic `EmailStr`).
- Extraction raises `ExtractionError` in `data_entry.extract` when no contact info is found.

### Change logging level
Set `LOG_LEVEL` in `.env` (`trace`, `debug`, `info`, `warn`, `error`). The CLI reads it at startup.

---

## CLI reference

Base command: `aurora`

| Command | Description |
| --- | --- |
| `aurora` (no args) | Print the package version |
| `aurora --help` | Show help |

---

## Docker

Build and run the container:

```bash
docker build -t aurora-automation .
docker run --rm aurora-automation
```

The image is based on `python:3.12-slim`, installs from `requirements.txt`, and runs the CLI.

---

## Troubleshooting

**`ModuleNotFoundError: No module named 'email_validator'`** — install the email extra: `pip install "pydantic[email]"` (already in `requirements.txt`).

**`pytest` reports coverage below 80%** — add tests for uncovered branches; check `pytest --cov=src --cov-report=term-missing`.

**`mypy` complains about missing stubs** — ensure dev deps are installed: `pip install -e ".[dev]"`.

**`ruff format --check` fails** — run `ruff format .` to rewrite files.

---

## Security

- No secrets are committed; `.env` is git-ignored.
- Environment variables are documented in `.env.example`.
- CI runs `pip-audit` on every push/PR to catch vulnerable dependencies.
- Report vulnerabilities privately.

---

## License

Released for use and modification. Replace branding and copy with your own before going live.