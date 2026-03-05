"""Generate AI rule files from Jinja2 templates."""

import os

from jinja2 import Environment, FileSystemLoader

TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), "templates")

PROCESS_LEVEL_RULES = {
    "Pipeline completa (TDD + boas praticas + fronteiras arquiteturais)": [
        "tdd",
        "best-practices",
        "boundaries",
        "minimal-changes",
    ],
    "Apenas testes (TDD enforcement)": [
        "tdd",
    ],
    "Apenas boas praticas (estilo, convencoes, minimal changes)": [
        "best-practices",
        "minimal-changes",
    ],
    "Minimo (apenas arquivo base da IA)": [],
}

RULE_FILE_NAMES = {
    "tdd": "tdd-enforcement",
    "best-practices": "best-practices",
    "boundaries": "architecture-boundaries",
    "minimal-changes": "minimal-changes",
}


def generate_files(
    output_dir: str,
    ais: list[str],
    language: str,
    process_level: str,
    project_name: str,
) -> list[str]:
    """Generate AI rule files based on user choices. Returns list of created files."""
    env = Environment(
        loader=FileSystemLoader(TEMPLATES_DIR),
        keep_trailing_newline=True,
    )
    context = {"project_name": project_name, "language": language}
    rules = PROCESS_LEVEL_RULES.get(process_level, [])
    created = []

    for ai in ais:
        if ai == "Claude Code":
            created += _generate_claude(env, context, rules, output_dir)
        elif ai == "Cursor":
            created += _generate_cursor(env, context, rules, output_dir)
        elif ai == "Codex":
            created += _generate_codex(env, context, output_dir)

    return created


def _write_file(path: str, content: str) -> bool:
    """Write content to path if file does not already exist. Returns True if written."""
    if os.path.exists(path):
        return False
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return True


def _generate_claude(
    env: Environment, context: dict, rules: list[str], output_dir: str
) -> list[str]:
    created = []
    base = env.get_template("claude/base.md.j2").render(**context)
    if _write_file(os.path.join(output_dir, "CLAUDE.md"), base):
        created.append("CLAUDE.md")

    for rule_key in rules:
        template_name = f"claude/rules/{rule_key}.md.j2"
        file_name = f"{RULE_FILE_NAMES[rule_key]}.md"
        content = env.get_template(template_name).render(**context)
        path = os.path.join(output_dir, ".claude", "rules", file_name)
        if _write_file(path, content):
            created.append(f".claude/rules/{file_name}")

    return created


def _generate_cursor(
    env: Environment, context: dict, rules: list[str], output_dir: str
) -> list[str]:
    created = []
    base = env.get_template("cursor/base.mdc.j2").render(**context)
    path = os.path.join(output_dir, ".cursor", "rules", "base.mdc")
    if _write_file(path, base):
        created.append(".cursor/rules/base.mdc")

    for rule_key in rules:
        template_name = f"cursor/rules/{rule_key}.mdc.j2"
        file_name = f"{RULE_FILE_NAMES[rule_key]}.mdc"
        content = env.get_template(template_name).render(**context)
        path = os.path.join(output_dir, ".cursor", "rules", file_name)
        if _write_file(path, content):
            created.append(f".cursor/rules/{file_name}")

    return created


def _generate_codex(env: Environment, context: dict, output_dir: str) -> list[str]:
    created = []
    content = env.get_template("codex/base.md.j2").render(**context)
    if _write_file(os.path.join(output_dir, "AGENTS.md"), content):
        created.append("AGENTS.md")
    return created
