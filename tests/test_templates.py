import os

from jinja2 import Environment, FileSystemLoader

TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), "..", "src", "aiscaffold", "templates")


def _render(template_path: str, **context) -> str:
    env = Environment(
        loader=FileSystemLoader(TEMPLATES_DIR),
        keep_trailing_newline=True,
    )
    tmpl = env.get_template(template_path)
    return tmpl.render(**context)


# --- Claude templates ---


class TestClaudeBaseTemplate:
    def test_renders_project_name(self):
        result = _render("claude/base.md.j2", project_name="my-app", language="Python")
        assert "my-app" in result

    def test_renders_language_python(self):
        result = _render("claude/base.md.j2", project_name="x", language="Python")
        assert "pytest" in result
        assert "ruff" in result

    def test_renders_language_node(self):
        result = _render("claude/base.md.j2", project_name="x", language="Node.js")
        assert "vitest" in result or "jest" in result
        assert "eslint" in result

    def test_references_claude_rules_dir(self):
        result = _render("claude/base.md.j2", project_name="x", language="Python")
        assert ".claude/rules/" in result

    def test_has_maintenance_section(self):
        result = _render("claude/base.md.j2", project_name="x", language="Python")
        lower = result.lower()
        assert "manuten" in lower or "maintenance" in lower or "atualiz" in lower

    def test_maintenance_mentions_this_file(self):
        result = _render("claude/base.md.j2", project_name="x", language="Python")
        assert "CLAUDE.md" in result


class TestClaudeRulesTemplates:
    def test_tdd_template_contains_red_green_refactor(self):
        result = _render("claude/rules/tdd.md.j2", language="Python")
        assert "RED" in result
        assert "GREEN" in result
        assert "REFACTOR" in result

    def test_tdd_template_python_uses_pytest(self):
        result = _render("claude/rules/tdd.md.j2", language="Python")
        assert "pytest" in result

    def test_tdd_template_node_uses_test_runner(self):
        result = _render("claude/rules/tdd.md.j2", language="Node.js")
        assert "vitest" in result or "jest" in result

    def test_boundaries_template_has_separation_of_concerns(self):
        result = _render("claude/rules/boundaries.md.j2", language="Python")
        assert (
            "separa" in result.lower() or "boundary" in result.lower() or "camada" in result.lower()
        )

    def test_best_practices_python_has_pep8(self):
        result = _render("claude/rules/best-practices.md.j2", language="Python")
        assert "PEP" in result or "pep" in result

    def test_best_practices_node_has_eslint(self):
        result = _render("claude/rules/best-practices.md.j2", language="Node.js")
        assert "eslint" in result or "ESLint" in result

    def test_minimal_changes_template_exists_and_renders(self):
        result = _render("claude/rules/minimal-changes.md.j2", language="Python")
        assert len(result) > 50

    # basic-commands rules were removed in favour of JSON configs
    def test_security_template_renders(self):
        result = _render("claude/rules/security.md.j2", language="Python")
        assert "segredos" in result.lower() or "injection" in result.lower() or "parametrizad" in result.lower()
        assert "subprocess" in result or "shell" in result.lower()

    def test_commits_cicd_template_renders(self):
        result = _render("claude/rules/commits-cicd.md.j2", language="Python")
        assert "commit" in result.lower() or "conventional" in result.lower()
        assert "CI" in result or "pipeline" in result.lower()


# --- Cursor templates ---


class TestCursorTemplates:
    def test_base_has_frontmatter(self):
        result = _render("cursor/base.mdc.j2", project_name="x", language="Python")
        assert "---" in result
        assert "alwaysApply" in result or "description" in result

    def test_base_has_maintenance_section(self):
        result = _render("cursor/base.mdc.j2", project_name="x", language="Python")
        lower = result.lower()
        assert "manuten" in lower or "maintenance" in lower or "atualiz" in lower

    def test_tdd_rule_has_glob_pattern(self):
        result = _render("cursor/rules/tdd.mdc.j2", language="Python")
        assert "globs" in result or "alwaysApply" in result

    def test_tdd_rule_python_references_pytest(self):
        result = _render("cursor/rules/tdd.mdc.j2", language="Python")
        assert "pytest" in result

    def test_tdd_rule_node_references_test_runner(self):
        result = _render("cursor/rules/tdd.mdc.j2", language="Node.js")
        assert "vitest" in result or "jest" in result

    def test_best_practices_has_frontmatter(self):
        result = _render("cursor/rules/best-practices.mdc.j2", language="Python")
        assert "---" in result

    def test_boundaries_has_frontmatter(self):
        result = _render("cursor/rules/boundaries.mdc.j2", language="Python")
        assert "---" in result

    def test_minimal_changes_has_frontmatter(self):
        result = _render("cursor/rules/minimal-changes.mdc.j2", language="Python")
        assert "---" in result

    # basic-commands rules were removed in favour of JSON configs

    def test_security_has_frontmatter_and_content(self):
        result = _render("cursor/rules/security.mdc.j2", language="Python")
        assert "---" in result
        assert "segredos" in result.lower() or "injection" in result.lower()

    def test_commits_cicd_has_frontmatter_and_content(self):
        result = _render("cursor/rules/commits-cicd.mdc.j2", language="Python")
        assert "---" in result
        assert "commit" in result.lower() or "feat" in result


# --- Codex templates ---


class TestCodexTemplates:
    def test_agents_md_renders_project_name(self):
        result = _render("codex/base.md.j2", project_name="my-api", language="Python")
        assert "my-api" in result

    def test_agents_md_python_has_commands(self):
        result = _render("codex/base.md.j2", project_name="x", language="Python")
        assert "pytest" in result
        assert "ruff" in result or "lint" in result.lower()

    def test_agents_md_node_has_commands(self):
        result = _render("codex/base.md.j2", project_name="x", language="Node.js")
        assert "npm" in result or "npx" in result

    def test_agents_md_has_tdd_section(self):
        result = _render("codex/base.md.j2", project_name="x", language="Python")
        assert "TDD" in result or "test" in result.lower()

    def test_agents_md_has_maintenance_section(self):
        result = _render("codex/base.md.j2", project_name="x", language="Python")
        lower = result.lower()
        assert "manuten" in lower or "maintenance" in lower or "atualiz" in lower

    def test_agents_md_has_security_and_commits_sections(self):
        result = _render("codex/base.md.j2", project_name="x", language="Python")
        assert "Security" in result or "Seguranca" in result or "seguranca" in result
        assert "Commits" in result or "CI/CD" in result

    def test_agents_md_basic_commands_mentions_sandbox(self):
        result = _render(
            "codex/base.md.j2", project_name="x", language="Python", rules_lang="en-US"
        )
        assert "sandbox" in result.lower() or "shell" in result.lower()

    def test_agents_md_rules_lang_en_renders_english(self):
        result = _render(
            "codex/base.md.j2",
            project_name="x",
            language="Python",
            rules_lang="en-US",
        )
        assert "Document Maintenance" in result
        assert "Always" in result or "Never" in result
        assert "One commit, one purpose" in result

    def test_claude_base_rules_lang_en_renders_english(self):
        result = _render(
            "claude/base.md.j2",
            project_name="x",
            language="Python",
            rules_lang="en-US",
        )
        assert "Mandatory Rules" in result
        assert "Commands" in result
        assert "living documents" in result or "Maintenance" in result
