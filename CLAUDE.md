# AI Scaffolding

Ferramenta CLI em Python que gera arquivos de regras para IAs de codificacao (Claude Code, Cursor, Codex) com base em boas praticas de XP e TDD, adaptados por linguagem e nivel de processo.

## Stack

- Python >=3.10, empacotado com hatchling
- CLI: click | Prompts: questionary | Templates: Jinja2
- Testes: pytest | Lint/Format: ruff | Types: mypy
- Estrutura src layout: `src/aiscaffold/`

## Comandos

```bash
# Instalar em modo dev
pip install -e .

# Executar CLI
python -m aiscaffold init

# Testes
python -m pytest tests/ -v

# Lint
ruff check src/ tests/
ruff format src/ tests/

# Type check
mypy src/
```

## Arquitetura

```
src/aiscaffold/
  cli.py          - Entry point CLI (click group + commands)
  prompts.py      - Perguntas interativas (questionary)
  generator.py    - Orquestra geracao de arquivos a partir dos templates
  templates/      - Templates Jinja2 organizados por IA/linguagem
tests/
  test_cli.py     - Testes do CLI com CliRunner
  test_prompts.py - Testes das opcoes e constantes
  test_generator.py - Testes de geracao de arquivos
```

## Regras Mandatorias

MANDATORY: Leia os arquivos em `.claude/rules/` antes de qualquer implementacao:

- `.claude/rules/tdd-enforcement.md` - Ciclo RED-GREEN-REFACTOR obrigatorio
- `.claude/rules/best-practices.md` - Convencoes Python e padrao do projeto
- `.claude/rules/architecture-boundaries.md` - Separacao de camadas e responsabilidades
- `.claude/rules/minimal-changes.md` - Escopo restrito de alteracoes

## Contexto do Projeto

- PLAN.md contem o planejamento completo das 4 fases
- DOCS.md contem a fundamentacao teorica (XP, TDD, regras de IA)
- Os templates Jinja2 em `src/aiscaffold/templates/` sao o produto final entregue ao usuario
- Este repositorio pratica dogfooding: usa suas proprias regras de IA
