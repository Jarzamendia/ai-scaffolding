from unittest.mock import patch

from click.testing import CliRunner

from aiscaffold.cli import main


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
        with patch("aiscaffold.cli.ask_user_choices", return_value=mock_choices):
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
        with patch("aiscaffold.cli.ask_user_choices", return_value=mock_choices):
            result = runner.invoke(main, ["init"])

        assert result.exit_code == 0
        assert "Codex" in result.output
        assert "Node.js" in result.output
        assert "Minimo" in result.output


class TestCLIDryRun:
    def test_dry_run_flag_exists(self):
        runner = CliRunner()
        result = runner.invoke(main, ["init", "--help"])
        assert "--dry-run" in result.output

    def test_dry_run_does_not_create_files(self, tmp_path):
        mock_choices = {
            "ais": ["Claude Code"],
            "language": "Python",
            "process_level": "Pipeline completa (TDD + boas praticas + fronteiras arquiteturais)",
        }
        runner = CliRunner()
        with patch("aiscaffold.cli.ask_user_choices", return_value=mock_choices):
            result = runner.invoke(main, ["init", "--output-dir", str(tmp_path), "--dry-run"])

        assert result.exit_code == 0
        assert not (tmp_path / "CLAUDE.md").exists()
        assert not (tmp_path / ".claude").exists()

    def test_dry_run_lists_files_that_would_be_created(self, tmp_path):
        mock_choices = {
            "ais": ["Claude Code"],
            "language": "Python",
            "process_level": "Minimo (apenas arquivo base da IA)",
        }
        runner = CliRunner()
        with patch("aiscaffold.cli.ask_user_choices", return_value=mock_choices):
            result = runner.invoke(main, ["init", "--output-dir", str(tmp_path), "--dry-run"])

        assert result.exit_code == 0
        assert "CLAUDE.md" in result.output

    def test_dry_run_shows_skip_for_existing_files(self, tmp_path):
        (tmp_path / "CLAUDE.md").write_text("existing")
        mock_choices = {
            "ais": ["Claude Code"],
            "language": "Python",
            "process_level": "Minimo (apenas arquivo base da IA)",
        }
        runner = CliRunner()
        with patch("aiscaffold.cli.ask_user_choices", return_value=mock_choices):
            result = runner.invoke(main, ["init", "--output-dir", str(tmp_path), "--dry-run"])

        assert result.exit_code == 0
        assert "skip" in result.output.lower() or "existe" in result.output.lower()


class TestCLIEntryPoints:
    def test_main_module_is_runnable(self):
        """python -m aiscaffold --help should work."""
        import subprocess
        import sys

        result = subprocess.run(
            [sys.executable, "-m", "aiscaffold", "--help"],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        assert "init" in result.stdout

    def test_script_entry_point_is_configured(self):
        """aiscaffold entry point should be defined in package metadata."""
        from importlib.metadata import distribution

        dist = distribution("aiscaffold")
        entry_points = [ep for ep in dist.entry_points if ep.group == "console_scripts"]
        names = [ep.name for ep in entry_points]
        assert "aiscaffold" in names

    def test_init_without_subcommand_shows_help(self):
        runner = CliRunner()
        result = runner.invoke(main, [])
        assert result.exit_code == 0
        assert "init" in result.output
