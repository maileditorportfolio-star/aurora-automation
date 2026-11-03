# Verification

Everything below is reproducible from a fresh clone.

```bash
python -m venv .venv
.venv\Scripts\activate   # or: source .venv/bin/activate
pip install -e ".[dev]"
pytest
ruff check .
ruff format --check .
mypy src
```