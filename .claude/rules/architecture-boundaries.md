# Architecture Boundaries

Regras de separacao de responsabilidades e limites entre camadas.

## Modulos e Responsabilidades

| Modulo | Responsabilidade | Nao deve |
|--------|-----------------|----------|
| `cli.py` | Parsing de comandos, orquestracao de alto nivel | Conter logica de geracao ou templates |
| `prompts.py` | Definicao de opcoes e interacao com usuario | Importar click ou acessar filesystem |
| `generator.py` | Carregar templates, renderizar e gravar arquivos | Fazer perguntas ao usuario ou parsing de CLI |
| `templates/` | Conteudo dos arquivos gerados (Jinja2) | Conter logica Python complexa |

## Regras de Fronteira

1. **Fluxo unidirecional:** `cli.py` -> `prompts.py` -> `cli.py` -> `generator.py` -> `templates/`
   - O CLI chama prompts, recebe respostas, passa para o generator.
   - O generator nunca chama prompts. Prompts nunca acessam o generator.

2. **Sem God Objects:** Nenhum modulo deve acumular multiplas responsabilidades.
   - Se `generator.py` crescer demais, extrair para submodulos (ex: `generator/claude.py`).

3. **Templates sao dados, nao logica:**
   - Templates Jinja2 usam apenas variaveis, condicionais simples e loops.
   - Logica de decisao (quais templates gerar, quais variaveis passar) fica no `generator.py`.

4. **Constantes centralizadas:**
   - Listas de opcoes (AI_CHOICES, LANGUAGE_CHOICES, PROCESS_LEVEL_CHOICES) vivem em `prompts.py`.
   - Mapeamentos de template (qual arquivo gerar para qual IA/nivel) vivem em `generator.py`.

5. **Sem imports circulares:**
   - `cli.py` importa `prompts.py` e `generator.py`.
   - `prompts.py` e `generator.py` nao importam `cli.py` nem um ao outro.
