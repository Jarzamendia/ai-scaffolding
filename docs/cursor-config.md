# Configurar Cursor: comandos sem pergunta e fetch de sites

Guia para configurar o Cursor de forma que o Agent **não pergunte** na execução de certos comandos e possa fazer **fetch** em sites permitidos. Baseado na [documentação oficial](https://cursor.com/docs/agent/terminal) (Terminal/Sandbox, [sandbox.json](https://cursor.com/docs/reference/sandbox), [Permissions CLI](https://cursor.com/docs/cli/reference/permissions)).

> **Nota:** quando você usa o `aiscaffold init` com Cursor selecionado, o projeto já começa com um `.cursor/sandbox.json` e um `.cursor/cli.json` básicos, pensados para testes/lint/git no workspace. Este guia mostra como **entender** esses arquivos e **personalizá-los** — não é necessário criar tudo do zero.

---

## 1. Comandos sem perguntar

### No editor (Cursor Settings)

**Onde:** **Settings > Cursor Settings > Agents > Auto-Run**

| Modo | Comportamento |
|------|----------------|
| **Run in Sandbox** | Comandos que cabem no sandbox rodam **automaticamente** (sem pergunta). Inclui testes, lint, leitura no workspace. Requer sandbox (macOS/Linux/WSL2 no Windows). |
| **Ask Every Time** | Toda execução de comando (e outras ferramentas) pede aprovação. |
| **Run Everything** | Tudo roda sem perguntar (menos seguro). |

Para não perguntar apenas para comandos específicos que saem do sandbox:

- **Command Allowlist** (na mesma área Agents): comandos listados podem rodar **fora do sandbox** sem confirmação.
- Quando um comando pede aprovação, use **"Add to allowlist"** para aprová-lo daqui pra frente.

**Resumo:** Ative **Run in Sandbox** para a maioria dos comandos de teste/lint/git rodarem sem pergunta. Para exceções, use a **Command Allowlist**.

### No Cursor CLI (agent via CLI)

Arquivos: **`~/.cursor/cli-config.json`** (global) ou **`.cursor/cli.json`** (por repositório).

Exemplo de permissões que autorizam comandos sem pedir aprovação:

```json
{
  "permissions": {
    "allow": [
      "Shell(pytest)",
      "Shell(npx)",
      "Shell(npm)",
      "Shell(git)",
      "Shell(ruff)",
      "Shell(mypy)"
    ]
  }
}
```

Sintaxe: `Shell(comando)` pelo primeiro token do comando; suporta padrões e `comando:args`. Ver [Permissions](https://cursor.com/docs/cli/reference/permissions).

---

## 2. Permitir fetch de alguns sites

### No editor (sandbox)

O acesso à rede do sandbox é controlado por:

1. **Settings > Agents > Auto-Run > Auto-run network access**
   - **sandbox.json Only**: só domínios em `sandbox.json`.
   - **sandbox.json + Defaults**: seu `sandbox.json` + lista padrão do Cursor (registries, GitHub, etc.).
   - **Allow All**: qualquer rede (menos seguro).

2. **Arquivo `sandbox.json`** (lista explícita de domínios)

Locais (per-repo tem prioridade sobre per-user):

- **`~/.cursor/sandbox.json`** (global)
- **`.cursor/sandbox.json`** (no repositório)

Exemplo para permitir apenas alguns sites:

```json
{
  "networkPolicy": {
    "default": "deny",
    "allow": [
      "docs.python.org",
      "*.github.com",
      "developer.mozilla.org",
      "stackoverflow.com"
    ]
  }
}
```

Sintaxe: domínio exato ou `*.dominio.com` para subdomínios. Ver [sandbox reference](https://cursor.com/docs/reference/sandbox).

### No Cursor CLI

No mesmo **`~/.cursor/cli-config.json`** ou **`.cursor/cli.json`**:

```json
{
  "permissions": {
    "allow": [
      "WebFetch(docs.python.org)",
      "WebFetch(*.github.com)",
      "WebFetch(developer.mozilla.org)"
    ]
  }
}
```

Sem entrada na allowlist, cada fetch pode pedir aprovação; com esses itens em `allow`, o fetch para esses domínios é aprovado automaticamente.

---

## 3. Onde cada coisa fica (resumo)

| Objetivo | Onde configurar |
|----------|-----------------|
| Comandos sem perguntar (editor) | **Settings > Cursor Settings > Agents > Auto-Run** (Run in Sandbox ou Run Everything) + **Command Allowlist** para exceções fora do sandbox |
| Comandos sem perguntar (CLI) | **`~/.cursor/cli-config.json`** ou **`.cursor/cli.json`** → `permissions.allow` com `Shell(...)` |
| Fetch de sites (editor, sandbox) | **`.cursor/sandbox.json`** (ou `~/.cursor/sandbox.json`) → `networkPolicy.allow` + modo de rede em Settings |
| Fetch de sites (CLI) | **`~/.cursor/cli-config.json`** ou **`.cursor/cli.json`** → `permissions.allow` com `WebFetch(dominio)` |
