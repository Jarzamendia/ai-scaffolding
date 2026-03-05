# AI Scaffolding - Plano de Implementacao v1

## Visao Geral

Ferramenta CLI em Python baseada em Cookiecutter que gera arquivos de regras para IAs de codificacao (Claude Code, Cursor, Codex) com base em boas praticas de XP e TDD, adaptados por linguagem de programacao e nivel de processo desejado.

O usuario executa um comando, responde a 3 perguntas interativas, e recebe os arquivos de regras gerados no diretorio atual.

---

## Arquitetura do Projeto

```
ai-scaffolding/
├── pyproject.toml                  # Configuracao do projeto (uv/pip)
├── README.md
├── DOCS.md
├── PLAN.md
├── src/
│   └── ai_scaffolding/
│       ├── __init__.py
│       ├── cli.py                  # Entry point CLI (click/typer)
│       ├── prompts.py              # Perguntas interativas ao usuario
│       ├── generator.py            # Orquestra a geracao dos arquivos
│       └── templates/              # Templates Jinja2 por IA x linguagem
│           ├── claude/
│           │   ├── base.md.j2          # CLAUDE.md base
│           │   ├── rules/
│           │   │   ├── tdd.md.j2
│           │   │   ├── boundaries.md.j2
│           │   │   ├── best-practices.md.j2
│           │   │   └── minimal-changes.md.j2
│           │   ├── python.md.j2        # Regras especificas Python
│           │   └── node.md.j2          # Regras especificas Node
│           ├── cursor/
│           │   ├── base.mdc.j2         # Regra raiz
│           │   ├── rules/
│           │   │   ├── tdd.mdc.j2
│           │   │   ├── boundaries.mdc.j2
│           │   │   ├── best-practices.mdc.j2
│           │   │   └── minimal-changes.mdc.j2
│           │   ├── python.mdc.j2
│           │   └── node.mdc.j2
│           └── codex/
│               ├── base.md.j2          # AGENTS.md base
│               ├── python.md.j2
│               └── node.md.j2
├── tests/
│   ├── __init__.py
│   ├── test_cli.py
│   ├── test_prompts.py
│   ├── test_generator.py
│   └── test_templates.py
└── .github/
    └── workflows/
        └── ci.yml                  # Lint + testes automaticos
```

---

## Fluxo do Usuario

```
$ ai-scaffold init

? Quais IAs voce pretende usar? (multi-select)
  [x] Claude Code
  [x] Cursor
  [ ] Codex (OpenAI)

? Qual linguagem do projeto? (single-select)
  > Python
    Node.js

? Qual nivel de processo? (single-select)
  > Pipeline completa (TDD + boas praticas + fronteiras arquiteturais)
    Apenas testes (TDD enforcement)
    Apenas boas praticas (estilo, convencoes, minimal changes)
    Minimo (apenas arquivo base da IA)
```

**Resultado:** Arquivos gerados no diretorio atual do usuario:

```
./
├── CLAUDE.md                       # (se Claude selecionado)
├── .claude/
│   └── rules/
│       ├── tdd-enforcement.md      # (se pipeline completa ou apenas testes)
│       ├── best-practices.md       # (se pipeline completa ou apenas boas praticas)
│       ├── architecture-boundaries.md
│       └── minimal-changes.md
├── .cursor/
│   └── rules/
│       ├── tdd-enforcement.mdc     # (se Cursor selecionado)
│       ├── best-practices.mdc
│       ├── architecture-boundaries.mdc
│       └── minimal-changes.mdc
└── AGENTS.md                       # (se Codex selecionado)
```

---

## Fases de Implementacao

### Fase 1 - Fundacao (Infraestrutura + CLI basico)

**Objetivo:** Projeto Python funcional com CLI que faz as 3 perguntas e imprime as respostas.

**Tarefas:**
1. Criar `pyproject.toml` com dependencias (click, jinja2, questionary, pytest)
2. Criar estrutura `src/ai_scaffolding/` com `__init__.py`
3. Implementar `cli.py` com comando `init` usando click
4. Implementar `prompts.py` com as 3 perguntas interativas usando questionary
5. Testes unitarios para prompts (mock de input)
6. Testes unitarios para CLI (click test runner)

**Criterio de aceite:** `ai-scaffold init` executa, faz as 3 perguntas e imprime as escolhas.

---

### Fase 2 - Templates Base

**Objetivo:** Criar os templates Jinja2 para cada IA com conteudo baseado no DOCS.md.

**Tarefas:**
1. Criar template `CLAUDE.md` base (limite de ~150 linhas, roteador para .claude/rules/)
2. Criar templates `.claude/rules/` (tdd, boundaries, best-practices, minimal-changes)
3. Criar template `AGENTS.md` base (contrato agonistico universal)
4. Criar templates `.cursor/rules/` com frontmatter YAML adequado (globs, description, alwaysApply)
5. Criar variantes por linguagem (Python: pytest/ruff/mypy, Node: vitest/eslint/typescript)
6. Testes de renderizacao dos templates (verificar que variaveis sao substituidas corretamente)

**Criterio de aceite:** Templates renderizam corretamente para todas as combinacoes de IA x linguagem x nivel.

---

### Fase 3 - Gerador de Arquivos

**Objetivo:** Conectar CLI + prompts + templates para gerar arquivos no disco.

**Tarefas:**
1. Implementar `generator.py` que recebe as escolhas e gera os arquivos
2. Logica de selecao de templates baseada no nivel de processo escolhido:
   - Pipeline completa: todos os arquivos de regras
   - Apenas testes: somente tdd-enforcement
   - Apenas boas praticas: best-practices + minimal-changes
   - Minimo: apenas arquivo base (CLAUDE.md / AGENTS.md / .cursor/rules/base.mdc)
3. Criar diretorios necessarios (.claude/rules/, .cursor/rules/)
4. Nao sobrescrever arquivos existentes sem confirmacao
5. Testes de integracao (gerar em tmpdir e verificar conteudo)

**Criterio de aceite:** `ai-scaffold init` gera os arquivos corretos no diretorio atual.

---

### Fase 4 - Polimento e Distribuicao

**Objetivo:** Tornar a ferramenta instalavel e publicavel.

**Tarefas:**
1. Configurar entry point no `pyproject.toml` (`[project.scripts]`)
2. Adicionar `--output-dir` flag opcional ao CLI
3. Adicionar `--dry-run` flag para preview dos arquivos que seriam gerados
4. Criar CI com GitHub Actions (lint com ruff, testes com pytest)
5. Atualizar README.md com instrucoes de instalacao e uso
6. Adicionar CLAUDE.md ao proprio projeto (dogfooding)

**Criterio de aceite:** `pip install .` funciona e `ai-scaffold init` esta disponivel globalmente.

---

## Decisoes Tecnicas

| Decisao | Escolha | Justificativa |
|---------|---------|---------------|
| Gerenciador de pacotes | uv | Rapido, moderno, resolve deps eficientemente |
| CLI framework | click | Maduro, bem documentado, test runner integrado |
| Perguntas interativas | questionary | Multi-select, single-select, UX rica no terminal |
| Templating | Jinja2 | Padrao da industria, usado pelo Cookiecutter internamente |
| Testes | pytest | Padrao Python, fixtures, parametrize, tmpdir |
| Lint/Format | ruff | Rapido, substitui flake8+black+isort |
| Type check | mypy | Padrao de mercado |

**Nota sobre Cookiecutter:** Apos analise, a abordagem com Jinja2 direto e mais adequada que Cookiecutter puro para este caso. Cookiecutter e otimizado para scaffolding de projetos inteiros a partir de um template fixo com `cookiecutter.json`. Nosso caso exige logica condicional complexa (multi-select de IAs, niveis de processo que filtram quais arquivos gerar), o que ficaria forcado no modelo do Cookiecutter. Usamos Jinja2 (a mesma engine do Cookiecutter) diretamente, mantendo controle total sobre a logica de geracao.

---

## Conteudo dos Templates (Resumo)

Baseado nas diretrizes do DOCS.md:

### CLAUDE.md (Roteador - max ~150 linhas)
- Proposito do projeto (placeholder para o usuario preencher)
- Stack tecnologica e convencoes
- Ponteiros para `.claude/rules/` com leitura mandatoria
- Comandos de build/test/lint especificos da linguagem

### .claude/rules/tdd-enforcement.md
- Ciclo RED-GREEN-REFACTOR obrigatorio
- Padrao AAA (Arrange-Act-Assert)
- Proibicao de implementacao sem teste previo
- Proibicao de alterar testes para perdoar codigo ruim

### .claude/rules/best-practices.md
- Convencoes de nomenclatura por linguagem
- Regras de imports e dependencias
- Tratamento de erros idiomatico

### .claude/rules/architecture-boundaries.md
- Separation of Concerns
- Proibicao de God Objects
- Regras de acoplamento entre camadas

### .claude/rules/minimal-changes.md
- Nao fazer refatoracoes nao solicitadas
- Nao adicionar features especulativas (gold plating)
- Alterar apenas o que foi pedido

### AGENTS.md
- Mesmo conteudo conceitual, formatado para o padrao AGENTS.md
- Comandos de build/test/lint
- Cascata hierarquica por diretorios

### .cursor/rules/*.mdc
- Mesmo conteudo conceitual com frontmatter YAML
- Globs patterns para escopo de aplicacao
- Tipos: alwaysApply, auto, file-pattern

---

## Ordem de Execucao Sugerida

1. **Fase 1** - 1 sessao de desenvolvimento
2. **Fase 2** - 1-2 sessoes (maior volume de conteudo nos templates)
3. **Fase 3** - 1 sessao
4. **Fase 4** - 1 sessao

Cada fase segue TDD: testes primeiro, implementacao depois, refactor ao final.

---

## Proximos Passos (v2 - futuro)

- Mais linguagens: Rust, Go, TypeScript (separado de Node)
- Mais IAs: GitHub Copilot, Windsurf, Aider
- Comando `ai-scaffold update` para atualizar regras sem sobrescrever customizacoes
- Comando `ai-scaffold doctor` para validar se os arquivos estao corretos
- Templates comunitarios via registry/plugin system
- Suporte a monorepos (regras por subdiretorio)
