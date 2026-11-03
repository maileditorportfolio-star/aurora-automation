"""CLI entry point for Aurora Automation."""

import logging
import os

import typer

app = typer.Typer(help="Aurora Automation CLI")

logging.basicConfig(level=getattr(logging, os.getenv("LOG_LEVEL", "INFO").upper(), logging.INFO))
logger = logging.getLogger(__name__)


@app.command()
def version() -> None:
    """Print the package version."""
    from aurora_automation import __version__

    typer.echo(__version__)


if __name__ == "__main__":
    app()
