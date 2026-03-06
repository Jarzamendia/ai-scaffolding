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
        "security",
        "commits-cicd",
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
    "security": "security",
    "commits-cicd": "commits-cicd",
}


def generate_files(
    output_dir: str,
    ais: list[str],
    language: str,
    process_level: str,
    project_name: str,
    rules_lang: str = "pt-BR",
    dry_run: bool = False,
) -> list[dict]:
    """Generate AI rule files based on user choices.

    Returns list of dicts with keys: path, status ("created" | "skipped").
    rules_lang: "pt-BR" or "en-US" for the language of generated rule content.
    """
    env = Environment(
        loader=FileSystemLoader(TEMPLATES_DIR),
        keep_trailing_newline=True,
    )
    context = {
        "project_name": project_name,
        "language": language,
        "rules_lang": rules_lang,
    }
    rules = PROCESS_LEVEL_RULES.get(process_level, [])
    results = []

    for ai in ais:
        if ai == "Claude Code":
            results += _generate_claude(env, context, rules, output_dir, dry_run)
        elif ai == "Cursor":
            results += _generate_cursor(env, context, rules, output_dir, dry_run)
        elif ai == "Codex":
            results += _generate_codex(env, context, output_dir, dry_run)

    return results


def _write_file(path: str, content: str, dry_run: bool) -> str:
    """Write content to path if file does not already exist.

    Returns "created", "skipped", or "would_create".
    """
    if os.path.exists(path):
        return "skipped"
    if dry_run:
        return "would_create"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return "created"


def _generate_claude(
    env: Environment, context: dict, rules: list[str], output_dir: str, dry_run: bool
) -> list[dict]:
    results = []
    base = env.get_template("claude/base.md.j2").render(**context)
    status = _write_file(os.path.join(output_dir, "CLAUDE.md"), base, dry_run)
    results.append({"path": "CLAUDE.md", "status": status})

    for rule_key in rules:
        template_name = f"claude/rules/{rule_key}.md.j2"
        file_name = f"{RULE_FILE_NAMES[rule_key]}.md"
        content = env.get_template(template_name).render(**context)
        path = os.path.join(output_dir, ".claude", "rules", file_name)
        status = _write_file(path, content, dry_run)
        results.append({"path": f".claude/rules/{file_name}", "status": status})

    return results


def _generate_cursor(
    env: Environment, context: dict, rules: list[str], output_dir: str, dry_run: bool
) -> list[dict]:
    results = []
    base = env.get_template("cursor/base.mdc.j2").render(**context)
    path = os.path.join(output_dir, ".cursor", "rules", "base.mdc")
    status = _write_file(path, base, dry_run)
    results.append({"path": ".cursor/rules/base.mdc", "status": status})

    for rule_key in rules:
        template_name = f"cursor/rules/{rule_key}.mdc.j2"
        file_name = f"{RULE_FILE_NAMES[rule_key]}.mdc"
        content = env.get_template(template_name).render(**context)
        path = os.path.join(output_dir, ".cursor", "rules", file_name)
        status = _write_file(path, content, dry_run)
        results.append({"path": f".cursor/rules/{file_name}", "status": status})

    return results


def _generate_codex(env: Environment, context: dict, output_dir: str, dry_run: bool) -> list[dict]:
    results = []
    content = env.get_template("codex/base.md.j2").render(**context)
    status = _write_file(os.path.join(output_dir, "AGENTS.md"), content, dry_run)
    results.append({"path": "AGENTS.md", "status": status})
    return results
