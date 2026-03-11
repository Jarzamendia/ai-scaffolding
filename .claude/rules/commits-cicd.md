# Commits and CI/CD

## Conventional Commits

**Sempre** utilize o padrão **Conventional Commits**. Formato: `tipo(escopo): descrição`.

**Tipos permitidos:** `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`.

**Certo:** `feat(auth): add JWT validation logic`

**Errado:** `fixed the login bug and also added some styles`

- **Atomicidade:** Um commit, uma mudança lógica.
- **Modo imperativo** no título (ex: "add", "fix", não "added", "fixed").
- **Título:** Máximo 50 caracteres. Corpo explica o **O quê** e o **Porquê**, não o "Como".

## CI/CD

- **Nunca** pule os testes no pipeline. **Sempre** verifique se testes e lint passam localmente antes de commit/push.
- Se o CI falhar após um push, **sua primeira prioridade** é analisar os logs e corrigir a falha. Não inicie novas tarefas com o pipeline "vermelho".
- **Ação obrigatória em falha:** (1) Leia o log de erro do CI. (2) Identifique se é ambiente, teste ou lint. (3) Proponha a correção exata com base na evidência do log.
- **Segredos:** Nunca inclua chaves, senhas ou segredos no código ou em arquivos versionados. Use variáveis de ambiente e mantenha `.env.example` atualizado (sem valores reais).
- **Branches protegidas:** Respeite as regras de proteção (ex: `main`). Use Pull Requests para integrar mudanças; não faça push direto para branches protegidas.
