# TDD Enforcement

Todo desenvolvimento neste repositorio segue obrigatoriamente o ciclo RED-GREEN-REFACTOR.

## Regras Inviolaveis

1. **NUNCA implemente codigo de producao sem um teste falhando primeiro.**
   - Antes de criar ou modificar qualquer arquivo em `src/`, deve existir um teste correspondente em `tests/` que falhe.

2. **Padrao AAA (Arrange-Act-Assert)**
   - Todo teste deve seguir a estrutura: preparar dados, executar acao, verificar resultado.
   - Nomes de teste devem descrever o comportamento esperado: `test_<acao>_<resultado_esperado>`.

3. **Fase RED: Escreva o teste primeiro**
   - Crie o teste descrevendo o comportamento desejado.
   - Execute `python -m pytest tests/ -v` e confirme que o teste falha.
   - O erro deve ser por ausencia de implementacao, nao por erro de sintaxe no teste.

4. **Fase GREEN: Implementacao minima**
   - Escreva apenas o codigo necessario para fazer o teste passar.
   - Nao adicione logica especulativa, tratamento de edge cases nao testados, ou features extras.
   - Execute `python -m pytest tests/ -v` e confirme que passa.

5. **Fase REFACTOR: Limpeza com rede de seguranca**
   - Somente apos GREEN, refatore para melhorar clareza ou eliminar duplicacao.
   - Todos os testes devem continuar passando apos refactor.

6. **NUNCA altere um teste para fazer codigo ruim passar.**
   - Se um teste falha apos implementacao, o problema esta no codigo, nao no teste.
   - Excecao: corrigir um teste genuinamente errado (requisito mudou).

## Comandos de Verificacao

```bash
# Executar todos os testes
python -m pytest tests/ -v

# Executar teste especifico
python -m pytest tests/test_cli.py::TestCLIInit::test_init_command_exists -v

# Executar com cobertura
python -m pytest tests/ --cov=ai_scaffolding --cov-report=term-missing
```
