import os

from jinja2 import Environment, FileSystemLoader

TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), "..", "src", "ai_scaffolding", "templates")


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


# --- Cursor templates ---


class TestCursorTemplates:
    def test_base_has_frontmatter(self):
        result = _render("cursor/base.mdc.j2", project_name="x", language="Python")
        assert "---" in result
        assert "alwaysApply" in result or "description" in result

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
