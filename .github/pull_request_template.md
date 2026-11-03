# Pull request

## Summary

<!-- What changes, and why. Link the issue or ADR when one exists. -->

## Test evidence

<!-- Paste the commands you ran and their result. -->

- [ ] `pytest`
- [ ] `ruff check .`
- [ ] `ruff format --check .`
- [ ] `mypy src`

## Checklist

- [ ] The behaviour change and the spec that pins it are in the same commit.
- [ ] `CHANGELOG.md` has an entry for user-visible changes.
- [ ] New environment variables are added to the matching `.env.example`.
- [ ] No `.env` files, credentials, or local data are included.
- [ ] The commit subject uses a conventional prefix and the diff stays focused.