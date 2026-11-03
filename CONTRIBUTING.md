# Contributing

1. Fork and create a feature branch.
2. Install deps: `pip install -r requirements.txt && pip install -e ".[dev]"`.
3. Run checks before committing: `pytest`, `ruff check .`, `ruff format --check .`, `mypy src`.
4. Use Conventional Commits (`feat:`, `fix:`, `chore:`).
5. Each feature/fix commit must include its tests.

No `.env` files, credentials, or local data should be committed.