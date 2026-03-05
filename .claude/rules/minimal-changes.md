# Minimal Changes Policy

Regras para manter o escopo de alteracoes restrito e previsivel.

## Principios

1. **Altere apenas o que foi pedido.**
   - Se a tarefa e "adicionar flag --dry-run", nao refatore o generator inteiro.
   - Se a tarefa e "corrigir bug no template X", nao melhore o template Y.

2. **Sem gold plating.**
   - Nao adicione features, parametros ou tratamentos que nao foram solicitados.
   - Nao crie abstracoes "para o futuro". Resolva o problema de hoje.

3. **Sem refatoracoes oportunistas.**
   - Nao renomeie variaveis, reorganize imports, ou mude formatacao de codigo que nao e parte da tarefa.
   - Se encontrar algo que precisa melhorar, reporte separadamente.

4. **Testes cirurgicos.**
   - Adicione testes apenas para o comportamento novo ou alterado.
   - Nao adicione testes retroativos para codigo existente que nao foi modificado.

5. **Um commit, um proposito.**
   - Cada alteracao deve ter um escopo claro e descritivel em uma frase.
   - Se precisar de multiplas mudancas, faca em etapas separadas.

6. **Respeite o codigo existente.**
   - Siga os padroes ja estabelecidos no arquivo que esta editando.
   - Nao mude estilo, convencoes ou estrutura de codigo que ja funciona.
