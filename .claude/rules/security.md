# Security and Sanitization

Regras imperativas para prevenir vulnerabilidades comuns (OWASP Top 10). Trate toda entrada de usuário e dados externos como potencialmente maliciosos.

## Prevenção de Injeção

**SQL / NoSQL:** **Sempre** utilize queries parametrizadas ou ORMs seguros. **Nunca** utilize concatenação de strings ou f-strings para construir consultas.

**Certo:** `db.execute("SELECT * FROM users WHERE id = ?", [user_id])`

**Errado:** `db.execute(f"SELECT * FROM users WHERE id = {user_id}")`

## Sanitização de Saída (XSS)

**Sempre** sanitize e escape dados dinâmicos antes de renderizá-los em contextos HTML. Use as funções de escape padrão do seu framework. **Nunca** utilize métodos que ignorem a segurança (ex: `dangerouslySetInnerHTML`) sem sanitização prévia rigorosa.

## Execução Segura de Comandos

Ao executar comandos de sistema, **sempre** utilize listas de argumentos. **Nunca** utilize `shell=True` ou concatenação de strings em comandos de shell.


**Certo:** `subprocess.run(["ls", "-l", diretorio])`

**Errado:** `subprocess.run(f"ls -l {diretorio}", shell=True)`


## Gestão de Segredos e PII

**Nunca** inclua segredos (chaves de API, senhas, tokens) ou Informações de Identificação Pessoal (PII) diretamente no código. **Sempre** utilize variáveis de ambiente ou gerenciadores de segredos seguros. **Nunca** registre informações sensíveis em logs.

## Boas Práticas Adicionais

- **Validação de entrada:** Sempre verifique formato, tipo e comprimento de dados recebidos.
- **Defaults seguros:** Prefira HTTPS, algoritmos de criptografia fortes; desabilite protocolos inseguros.
- **Menor privilégio:** Código e configurações devem operar com o mínimo de permissão necessária.
