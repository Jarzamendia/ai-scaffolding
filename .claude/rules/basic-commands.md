# Basic Commands


Regras de uso de ferramentas e comandos permitidos para o Claude Code neste workspace.

## Explorar o Codebase

- Use a ferramenta `Glob` para buscar arquivos por padrão (ex: `**/*.py`, `src/**/*.ts`). **Não** use `find` ou `ls` pelo Bash.
- Use a ferramenta `Grep` para buscar conteúdo em arquivos. **Não** use `grep` ou `rg` pelo Bash.
- Use a ferramenta `Read` para ler arquivos. **Não** use `cat`, `head` ou `tail` pelo Bash.
- Sempre leia os arquivos que pretende alterar **antes** de editá-los.

## Editar Arquivos

- Use a ferramenta `Edit` para modificações. **Não** use `sed` ou `awk` pelo Bash.
- Use a ferramenta `Write` apenas para criar arquivos novos. Prefira `Edit` para arquivos existentes.
- **Não** crie arquivos a menos que seja estritamente necessário para a tarefa.

## Executar Comandos (Bash)

Use a ferramenta `Bash` exclusivamente para execução no shell: testes, lint, type check e build.


```bash
# Testes
python -m pytest tests/ -v

# Lint e formatação
ruff check .
ruff format .

# Type check
mypy src/
```


- **Sempre** rode os testes antes de considerar uma mudança concluída.
- **Sempre** rode o lint após modificar código.
- Não reporte sucesso se testes ou lint estiverem falhando. Analise a falha, corrija e rode novamente.

## Git (somente leitura por padrão)

- Você **pode** rodar comandos git de leitura pelo Bash para entender o estado do repositório:
  - `git status` para ver arquivos modificados e não rastreados.
  - `git diff` para inspecionar as mudanças atuais.
  - `git log --oneline -10` para ver commits recentes.
- **NÃO** execute `git add`, `git commit`, `git push` ou qualquer comando git destrutivo a menos que o usuário peça explicitamente.
- Quando o usuário pedir para commitar, siga Conventional Commits e nunca pule hooks (`--no-verify`).

