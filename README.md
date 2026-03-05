# AI Scaffolding

CLI tool that generates AI coding rule files for your projects. Supports **Claude Code**, **Cursor**, and **OpenAI Codex** with language-specific templates based on XP and TDD best practices.

## What it does

Run a single command, answer 3 questions, and get pre-configured AI rule files generated in your project directory:

- **Claude Code**: `CLAUDE.md` + `.claude/rules/` (tdd, boundaries, best-practices, minimal-changes)
- **Cursor**: `.cursor/rules/` with YAML frontmatter (`.mdc` files)
- **Codex**: `AGENTS.md` with setup, commands, and development rules

## Install

```bash
pip install -e .
```

## Usage

```bash
# Interactive mode - generates files in current directory
python -m ai_scaffolding init

# Specify output directory
python -m ai_scaffolding init --output-dir ./my-project

# Preview without creating files
python -m ai_scaffolding init --dry-run
```

### Interactive prompts

```
? Quais IAs voce pretende usar? (multi-select)
  [x] Claude Code
  [x] Cursor
  [ ] Codex

? Qual linguagem do projeto? (single-select)
  > Python
    Node.js

? Qual nivel de processo? (single-select)
  > Pipeline completa (TDD + boas praticas + fronteiras arquiteturais)
    Apenas testes (TDD enforcement)
    Apenas boas praticas (estilo, convencoes, minimal changes)
    Minimo (apenas arquivo base da IA)
```

## Process levels

| Level | What gets generated |
|-------|-------------------|
| **Pipeline completa** | All rule files: TDD enforcement, best practices, architecture boundaries, minimal changes |
| **Apenas testes** | Only TDD enforcement rules |
| **Apenas boas praticas** | Best practices + minimal changes rules |
| **Minimo** | Only the base file (CLAUDE.md / AGENTS.md / base.mdc) |

## Languages supported

- **Python**: pytest, ruff, mypy
- **Node.js**: vitest, eslint, prettier, tsc

## Development

```bash
# Install in dev mode
pip install -e .

# Run tests
python -m pytest tests/ -v

# Lint
ruff check src/ tests/
ruff format src/ tests/
```

## License

MIT
