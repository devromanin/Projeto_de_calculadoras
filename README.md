# Projeto de Calculadoras


Projeto em Python que reúne diferentes calculadoras com foco em boas práticas de backend, tipagem, validação de dados, regras de negócio e testes unitários.

O objetivo é simular cenários reais de APIs, incluindo tratamento correto de erros e respostas padronizadas.


---

## 📁 Estrutura do Projeto


src/  
Contém todo o código-fonte da aplicação, incluindo:

- calculadoras  
- interfaces  
- tratamento de erros personalizados  


tests/  
Contém os testes unitários escritos com pytest, cobrindo:

- validação de entrada  
- regras de negócio  
- cenários de sucesso e falha  


---

## ⚙️ Funcionalidades


O projeto possui múltiplas calculadoras, cada uma representando um fluxo diferente de processamento de dados:

- Calculator1  
- Calculator2  
- Calculator3  
- Calculator4  


Cada calculadora implementa:

- validação de dados de entrada  
- processamento de cálculos (média, variância, etc.)  
- tratamento de erros HTTP  
- retorno de respostas estruturadas  


---

## 🚨 Tratamento de Erros


O projeto simula erros comuns em APIs REST:

400 – Bad Request  
Usado quando uma regra de negócio é violada.

422 – Unprocessable Entity  
Usado quando o corpo da requisição está mal formatado ou inválido.

As exceções são personalizadas e cobertas por testes unitários.


---

## 🧪 Testes


Os testes são implementados com pytest e utilizam mocks para simular requests e dependências externas, garantindo isolamento da lógica de negócio.

Para executar os testes, rode na raiz do projeto:

python -m pytest


---


## 🛠️ Tecnologias Utilizadas


- Python 3  
- typing (tipagem estática)  
- pytest  
- Arquitetura orientada a classes  
- Injeção de dependência  
- Exceções customizadas  

