# 🏢 Auditoria de Orçamentos Corporativos (Python)
 
[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/status-concluído-brightgreen.svg)]()
 
## 📖 Sobre o Projeto
Este projeto foi desenvolvido como parte da disciplina de Programação de Computadores do curso de Análise e Desenvolvimento. O objetivo do script é processar e calcular o orçamento de uma estrutura organizacional complexa (dicionários aninhados) de uma multinacional, aplicando regras de negócio dinâmicas e auditoria de execução.
 
A solução foi arquitetada utilizando conceitos avançados de Python para garantir flexibilidade, performance e rastreabilidade.
 
## 🚀 Funcionalidades
- **Cálculo Hierárquico:** Varredura completa da estrutura corporativa, independentemente do nível de profundidade.
- **Filtros Dinâmicos:** Capacidade de ignorar setores específicos e todos os seus subsetores na hora do cálculo financeiro.
- **Conversão de Câmbio:** Suporte a parâmetros opcionais para conversão de moedas em tempo de execução.
- **Sistema de Auditoria:** Monitoramento automatizado de tempo de execução e registro (logging) dos parâmetros utilizados na transação financeira.
 
## 🛠️ Tecnologias e Conceitos Aplicados
Este projeto foi construído utilizando Python puro (Standard Library), com foco nos seguintes paradigmas e recursos:
* **Funções Recursivas (Recursion):** Utilizadas para a navegação na árvore de dados (dicionários aninhados).
* **Decorators:** Implementação do `@auditor` para injetar comportamentos de log e cronometragem sem modificar a lógica de negócios.
* **Empacotamento de Argumentos (`*args` e `**kwargs`):** Utilizados tanto no decorator quanto na função principal para permitir a passagem dinâmica de departamentos a serem ignorados e taxas de câmbio.
 
## ⚙️ Como Executar
 
### Pré-requisitos
* Python 3.8 ou superior instalado.
 
### Passo a Passo
1. Clone este repositório:
   ```bash
   git clone https://github.com/Ricardo-Rufino-Projetos/portfolio-ricardo-oliveira-rufino
   ```
2. Acesse a pasta do projeto:
   ```bash
   cd projeto_auditoria_de_recursos_corporativos
   ```
3. Execute o script principal:
   ```bash
   python projeto_auditoria_de_recursos_corporativos.py
   ```
 
## 🧠 Lógica e Estrutura do Código
Breve explicação de como o código foi organizado:
A lógica do código foi desenvolver uma forma de percorrer toda a estrutura financeira da empresa, mesmo com vários níveis de departamentos e subdepartamentos. Para isso, foi utilizada recursividade, permitindo que a função percorresse automaticamente cada parte do dicionário até encontrar os valores numéricos e realizar a soma do orçamento total. Também foram utilizados decorators para registrar a auditoria do processamento e medir o tempo de execução do sistema.

* **Dados:** Os dados simulados da empresa foram estruturados em um dicionário aninhado, representando a hierarquia da empresa. A estrutura começa pela chave principal "Matriz", que representa a sede da empresa. Dentro dela existem vários departamentos, como "TI", "RH", "Financeiro" e "Logistica"...
 
## 👤 Autor
 
* **Ricardo Oliveira Rufino** * LinkedIn: (https://www.linkedin.com/in/ricardo-oliveira-74bb73186)
* E-mail: rickoliveira20014@gmail.com
 
---
*Projeto acadêmico com foco na aplicação prática de conceitos avançados da linguagem Python.*
