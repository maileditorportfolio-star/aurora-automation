from typer.testing import CliRunner

from aurora_automation.cli import app


def test_cli_version():
    runner = CliRunner()
    result = runner.invoke(app, [])
    assert result.exit_code == 0
    assert result.stdout.strip() != ""