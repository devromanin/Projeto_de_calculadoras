Projeto de Calculadoras

Projeto em Python que reúne diferentes calculadoras com foco em boas práticas de backend, tipagem, validação de dados, regras de negócio e testes unitários.
A ideia é simular cenários reais de APIs, incluindo tratamento adequado de erros e respostas padronizadas.

📁 Estrutura do Projeto

src/
Contém todo o código-fonte da aplicação:

calculadoras

interfaces

tratamento de erros personalizados

tests/
Contém os testes unitários escritos com pytest, cobrindo:

validações de entrada

regras de negócio

cenários de sucesso e falha

⚙️ Funcionalidades

O projeto possui múltiplas calculadoras, cada uma representando um fluxo diferente de processamento de dados:

Calculator1

Calculator2

Calculator3

Calculator4

Cada calculadora implementa:

validação de dados de entrada

processamento de cálculos (média, variância, etc.)

tratamento de erros HTTP

retorno de respostas estruturadas

🚨 Tratamento de Erros

O projeto simula erros comuns de APIs REST:

400 – Bad Request
Usado quando a regra de negócio é violada

422 – Unprocessable Entity
Usado quando o corpo da requisição está mal formatado

As exceções são personalizadas e testadas com pytest.

🧪 Testes

Os testes são feitos com pytest e utilizam mocks para simular requests e dependências externas, garantindo isolamento da lógica.

Para rodar os testes, execute na raiz do projeto:

python -m pytest
