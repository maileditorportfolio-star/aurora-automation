# AGENTS.md — Aurora Automation (local memory)

Project memory for coding agents working in this repo. Read this first.

## Project snapshot

- **Repo**: `aurora-automation` — Python package for AI agents and automation workflows.
- **Source**: `src/aurora_automation/` (src layout)
- **Workflows**: `src/aurora_automation/workflows/` — email_triage, data_entry, research
- **Tests**: `tests/` (pytest)
- **Toolchain**: Python 3.10+, ruff, mypy, pytest

## Quick start

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -e ".[dev]"
cp .env.example .env
pytest
```

## Verify before you hand work back

```powershell
pytest
ruff check .
ruff format --check .
mypy src
```

## Conventions

- **Git**: Conventional Commits (`feat:`, `fix:`, `chore:`), one logical change per commit, never commit `.env` or secrets.
- **Formatting**: ruff, 100 cols, 4-space indent.
- **Naming**: snake_case modules/functions, PascalCase classes.
- **Tests**: every behaviour change ships with a spec in the same commit.