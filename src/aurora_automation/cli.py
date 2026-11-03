"""CLI entry point for Aurora Automation."""

import typer

app = typer.Typer(help="Aurora Automation CLI")


@app.command()
def version() -> None:
    """Print the package version."""
    from aurora_automation import __version__

    typer.echo(__version__)


if __name__ == "__main__":
    app()
