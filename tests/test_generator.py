from unittest.mock import patch

from click.testing import CliRunner

from aiscaffold.generator import generate_files


class TestGeneratorClaude:
    def test_generates_claude_md(self, tmp_path):
        generate_files(
            output_dir=str(tmp_path),
            ais=["Claude Code"],
            language="Python",
            process_level="Pipeline completa (TDD + boas praticas + fronteiras arquiteturais)",
            project_name="test-project",
        )
        assert (tmp_path / ".claude" / "CLAUDE.md").exists()
        assert (tmp_path / ".claude" / "commands.json").exists()
        assert (tmp_path / ".claude" / "network.json").exists()

    def test_claude_md_contains_project_name(self, tmp_path):
        generate_files(
            output_dir=str(tmp_path),
            ais=["Claude Code"],
            language="Python",
            process_level="Pipeline completa (TDD + boas praticas + fronteiras arquiteturais)",
            project_name="my-app",
        )
        content = (tmp_path / ".claude" / "CLAUDE.md").read_text()
        assert "my-app" in content

    def test_full_pipeline_generates_all_rules(self, tmp_path):
        generate_files(
            output_dir=str(tmp_path),
            ais=["Claude Code"],
            language="Python",
            process_level="Pipeline completa (TDD + boas praticas + fronteiras arquiteturais)",
            project_name="x",
        )
        rules_dir = tmp_path / ".claude" / "rules"
        assert (rules_dir / "tdd-enforcement.md").exists()
        assert (rules_dir / "best-practices.md").exists()
        assert (rules_dir / "architecture-boundaries.md").exists()
        assert (rules_dir / "minimal-changes.md").exists()
        assert (rules_dir / "security.md").exists()
        assert (rules_dir / "commits-cicd.md").exists()

    def test_tests_only_generates_only_tdd(self, tmp_path):
        generate_files(
            output_dir=str(tmp_path),
            ais=["Claude Code"],
            language="Python",
            process_level="Apenas testes (TDD enforcement)",
            project_name="x",
        )
        rules_dir = tmp_path / ".claude" / "rules"
        assert (rules_dir / "tdd-enforcement.md").exists()
        assert not (rules_dir / "best-practices.md").exists()
        assert not (rules_dir / "architecture-boundaries.md").exists()
        assert not (rules_dir / "minimal-changes.md").exists()
        assert not (rules_dir / "security.md").exists()
        assert not (rules_dir / "commits-cicd.md").exists()

    def test_best_practices_only_generates_practices_and_minimal(self, tmp_path):
        generate_files(
            output_dir=str(tmp_path),
            ais=["Claude Code"],
            language="Python",
            process_level="Apenas boas praticas (estilo, convencoes, minimal changes)",
            project_name="x",
        )
        rules_dir = tmp_path / ".claude" / "rules"
        assert not (rules_dir / "tdd-enforcement.md").exists()
        assert (rules_dir / "best-practices.md").exists()
        assert not (rules_dir / "architecture-boundaries.md").exists()
        assert (rules_dir / "minimal-changes.md").exists()
        assert not (rules_dir / "security.md").exists()
        assert not (rules_dir / "commits-cicd.md").exists()

    def test_minimum_generates_only_base(self, tmp_path):
        generate_files(
            output_dir=str(tmp_path),
            ais=["Claude Code"],
            language="Python",
            process_level="Minimo (apenas arquivo base da IA)",
            project_name="x",
        )
        assert (tmp_path / ".claude" / "CLAUDE.md").exists()
        assert not (tmp_path / ".claude" / "rules").exists()


class TestGeneratorCursor:
    def test_generates_cursor_base(self, tmp_path):
        generate_files(
            output_dir=str(tmp_path),
            ais=["Cursor"],
            language="Python",
            process_level="Pipeline completa (TDD + boas praticas + fronteiras arquiteturais)",
            project_name="x",
        )
        rules_dir = tmp_path / ".cursor" / "rules"
        assert (rules_dir / "base.mdc").exists()
        assert (tmp_path / ".cursor" / "sandbox.json").exists()
        assert (tmp_path / ".cursor" / "cli.json").exists()

    def test_full_pipeline_generates_all_cursor_rules(self, tmp_path):
        generate_files(
            output_dir=str(tmp_path),
            ais=["Cursor"],
            language="Python",
            process_level="Pipeline completa (TDD + boas praticas + fronteiras arquiteturais)",
            project_name="x",
        )
        rules_dir = tmp_path / ".cursor" / "rules"
        assert (rules_dir / "tdd-enforcement.mdc").exists()
        assert (rules_dir / "best-practices.mdc").exists()
        assert (rules_dir / "architecture-boundaries.mdc").exists()
        assert (rules_dir / "minimal-changes.mdc").exists()
        assert (rules_dir / "security.mdc").exists()
        assert (rules_dir / "commits-cicd.mdc").exists()
        assert (tmp_path / ".cursor" / "sandbox.json").exists()
        assert (tmp_path / ".cursor" / "cli.json").exists()

    def test_minimum_generates_only_base(self, tmp_path):
        generate_files(
            output_dir=str(tmp_path),
            ais=["Cursor"],
            language="Python",
            process_level="Minimo (apenas arquivo base da IA)",
            project_name="x",
        )
        rules_dir = tmp_path / ".cursor" / "rules"
        assert (rules_dir / "base.mdc").exists()
        assert not (rules_dir / "tdd-enforcement.mdc").exists()


class TestGeneratorCodex:
    def test_generates_agents_md(self, tmp_path):
        generate_files(
            output_dir=str(tmp_path),
            ais=["Codex"],
            language="Python",
            process_level="Pipeline completa (TDD + boas praticas + fronteiras arquiteturais)",
            project_name="my-api",
        )
        assert (tmp_path / "AGENTS.md").exists()
        content = (tmp_path / "AGENTS.md").read_text()
        assert "my-api" in content

    def test_node_agents_md_has_npm(self, tmp_path):
        generate_files(
            output_dir=str(tmp_path),
            ais=["Codex"],
            language="Node.js",
            process_level="Pipeline completa (TDD + boas praticas + fronteiras arquiteturais)",
            project_name="x",
        )
        content = (tmp_path / "AGENTS.md").read_text()
        assert "npm" in content or "npx" in content


class TestGeneratorMultipleAIs:
    def test_generates_all_selected_ais(self, tmp_path):
        generate_files(
            output_dir=str(tmp_path),
            ais=["Claude Code", "Cursor", "Codex"],
            language="Python",
            process_level="Pipeline completa (TDD + boas praticas + fronteiras arquiteturais)",
            project_name="full-project",
        )
        assert (tmp_path / ".claude" / "CLAUDE.md").exists()
        assert (tmp_path / ".cursor" / "rules" / "base.mdc").exists()
        assert (tmp_path / "AGENTS.md").exists()

    def test_does_not_generate_unselected_ais(self, tmp_path):
        generate_files(
            output_dir=str(tmp_path),
            ais=["Claude Code"],
            language="Python",
            process_level="Pipeline completa (TDD + boas praticas + fronteiras arquiteturais)",
            project_name="x",
        )
        assert (tmp_path / ".claude" / "CLAUDE.md").exists()
        assert not (tmp_path / ".cursor").exists()
        assert not (tmp_path / "AGENTS.md").exists()


class TestGeneratorNoOverwrite:
    def test_does_not_overwrite_existing_file(self, tmp_path):
        existing = tmp_path / ".claude" / "CLAUDE.md"
        existing.parent.mkdir(parents=True, exist_ok=True)
        existing.write_text("my custom content")

        generate_files(
            output_dir=str(tmp_path),
            ais=["Claude Code"],
            language="Python",
            process_level="Minimo (apenas arquivo base da IA)",
            project_name="x",
        )
        assert existing.read_text() == "my custom content"


class TestCLIIntegration:
    def test_init_calls_generator(self, tmp_path):
        from aiscaffold.cli import main

        mock_choices = {
            "ais": ["Claude Code"],
            "language": "Python",
            "process_level": "Minimo (apenas arquivo base da IA)",
            "rules_lang": "pt-BR",
        }
        runner = CliRunner()
        with patch("aiscaffold.cli.ask_user_choices", return_value=mock_choices):
            result = runner.invoke(main, ["init", "--output-dir", str(tmp_path)])

        assert result.exit_code == 0
        assert (tmp_path / ".claude" / "CLAUDE.md").exists()
