# aiscaffold

CLI tool that generates AI coding rule files for your projects. Supports **Claude Code**, **Cursor**, and **OpenAI Codex** with language-specific templates based on XP and TDD best practices.

## What it does

Run a single command, answer 4 questions, and get pre-configured AI rule files generated in your project directory:

- **Claude Code**: `.claude/CLAUDE.md` + `.claude/rules/` (tdd, boundaries, best-practices, minimal-changes, security, commits-cicd) + `.claude/commands.json` + `.claude/network.json`
- **Cursor**: `.cursor/rules/` with YAML frontmatter (`.mdc` files)
- **Codex**: `AGENTS.md` with setup, commands, and development rules

## Install

### Recommended: pipx (isolated, works globally)

```bash
pipx install git+https://github.com/Jarzamendia/ai-scaffolding.git
```

### Alternative: pip

```bash
pip install git+https://github.com/Jarzamendia/ai-scaffolding.git
```

### From source

```bash
git clone https://github.com/Jarzamendia/ai-scaffolding.git
cd ai-scaffolding
pip install .
```

After installing, `aiscaffold` is available globally from any directory.

> **Troubleshooting**: If `aiscaffold` is not found after `pip install`, your Python Scripts directory may not be in PATH. Either use `pipx` (recommended) or run via `python -m aiscaffold` instead.

## Usage

```bash
# From any directory
aiscaffold init

# Specify output directory
aiscaffold init --output-dir ./my-project

# Preview without creating files
aiscaffold init --dry-run

# Alternative (always works)
python -m aiscaffold init
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
    ...

? Em qual idioma devem ser geradas as regras? (single-select)
  > Português (Brasil)
    English
```

Rules can be generated in **Portuguese (Brazil)** or **English**. The CLI prompts remain in Portuguese.

## Process levels

| Level | What gets generated |
|-------|-------------------|
| **Pipeline completa** | All rule files: TDD, best practices, architecture boundaries, minimal changes, security, commits & CI/CD |
| **Apenas testes** | Only TDD enforcement rules |
| **Apenas boas praticas** | Best practices + minimal changes rules |
| **Minimo** | Only the base file (`.claude/CLAUDE.md` / `AGENTS.md` / `base.mdc`) |

## Languages supported

- **Python**: pytest, ruff, mypy
- **Node.js**: vitest, eslint, prettier, tsc

## Cursor: commands and network

When you select **Cursor** in `aiscaffold init`, the tool already generates:

- `.cursor/rules/` with the base rules and all rule files
- `.cursor/sandbox.json` with a safe default `networkPolicy` (deny by default, allow registries/docs)
- `.cursor/cli.json` with a basic `permissions.allow` for running tests/lint/type-check and basic git commands on the workspace

For details on how Cursor interprets these files, and how to customize them further (auto-run modes, extra allowlists, advanced network policies), see **[docs/cursor-config.md](docs/cursor-config.md)**.

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
