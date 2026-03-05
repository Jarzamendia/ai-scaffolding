from unittest.mock import patch

from click.testing import CliRunner

from ai_scaffolding.cli import main


class TestCLIInit:
    def test_init_command_exists(self):
        runner = CliRunner()
        result = runner.invoke(main, ["init", "--help"])
        assert result.exit_code == 0
        assert "init" in result.output.lower() or "Usage" in result.output

    def test_init_runs_prompts_and_shows_summary(self):
        mock_choices = {
            "ais": ["Claude Code", "Cursor"],
            "language": "Python",
            "process_level": "Pipeline completa (TDD + boas praticas + fronteiras arquiteturais)",
        }
        runner = CliRunner()
        with patch("ai_scaffolding.cli.ask_user_choices", return_value=mock_choices):
            result = runner.invoke(main, ["init"])

        assert result.exit_code == 0
        assert "Claude Code" in result.output
        assert "Cursor" in result.output
        assert "Python" in result.output
        assert "Pipeline completa" in result.output

    def test_init_shows_all_selected_ais(self):
        mock_choices = {
            "ais": ["Claude Code", "Cursor", "Codex"],
            "language": "Node.js",
            "process_level": "Minimo (apenas arquivo base da IA)",
        }
        runner = CliRunner()
        with patch("ai_scaffolding.cli.ask_user_choices", return_value=mock_choices):
            result = runner.invoke(main, ["init"])

        assert result.exit_code == 0
        assert "Codex" in result.output
        assert "Node.js" in result.output
        assert "Minimo" in result.output
