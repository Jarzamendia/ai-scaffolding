# Best Practices - Python

Convencoes e padroes obrigatorios para este projeto.

## Estilo de Codigo

- Seguir PEP 8 e convencoes do ruff.
- Line length maximo: 100 caracteres (configurado no pyproject.toml).
- Usar snake_case para funcoes e variaveis, PascalCase para classes.
- Strings com aspas duplas.
- Imports organizados: stdlib > terceiros > locais, separados por linha em branco.

## Estrutura do Projeto

- Codigo de producao em `src/ai_scaffolding/`.
- Testes em `tests/`, espelhando a estrutura de `src/`.
- Templates Jinja2 em `src/ai_scaffolding/templates/`, organizados por IA.
- Cada modulo tem uma responsabilidade clara e unica.

## Dependencias

- Usar apenas dependencias declaradas no `pyproject.toml`.
- Nao introduzir novas dependencias sem justificativa explicita.
- Preferir stdlib quando possivel.

## Tratamento de Erros

- Usar excecoes especificas, nunca `except Exception` generico.
- Erros de input do usuario devem gerar mensagens claras via `click.echo` ou `click.ClickException`.
- Nao silenciar erros com `pass` em blocos except.

## Testes

- Usar pytest como runner exclusivo.
- Agrupar testes em classes por contexto (ex: `TestCLIInit`, `TestGenerator`).
- Usar `tmp_path` fixture do pytest para testes que escrevem no disco.
- Mockar I/O externo (questionary, filesystem) com `unittest.mock.patch`.
- Usar `CliRunner` do click para testes de CLI.

## Templates Jinja2

- Extensao `.j2` para todos os templates.
- Variaveis de contexto documentadas no topo do template como comentario.
- Nao colocar logica complexa nos templates; manter no `generator.py`.
