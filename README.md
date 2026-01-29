Projeto de Calculadoras

Este repositório contém um conjunto de calculadoras desenvolvidas em Python com foco em boas práticas de programação, tipagem estática, validações e testes unitários. O projeto simula regras de negócio comuns em APIs, incluindo tratamento adequado de erros e respostas padronizadas.

Funcionalidades

O projeto conta com múltiplas calculadoras, cada uma representando um cenário diferente de processamento de dados:

Calculator1, Calculator2, Calculator3 e Calculator4

Validação de entrada de dados

Cálculo de métricas como média e variância

Tratamento de erros HTTP:

400 (Bad Request) para regras de negócio inválidas

422 (Unprocessable Entity) para erros de entrada

Respostas formatadas em padrão consistente

Testes

Os testes foram escritos utilizando pytest e utilizam mocks para simular requests e dependências externas.

Para executar os testes, rode na raiz do projeto:

python -m pytest

Exemplo de Uso

Exemplo de chamada da Calculator4:

request = { "numbers": [10, 20, 30] }
resultado = Calculator4(driver_handler).calculate(request)

Resposta esperada:

{
"data": {
"Calculator": 4,
"value": 20.0,
"Success": true
}
}

Tecnologias e Conceitos

Python 3

Tipagem com typing

Arquitetura orientada a classes

Injeção de dependência

Testes unitários com pytest

Exceções customizadas para simular erros HTTP
