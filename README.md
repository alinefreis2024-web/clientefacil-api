# ClienteFácil API

API desenvolvida para o MVP da Sprint II da pós-graduação em Desenvolvimento Full Stack da PUC-Rio.

O ClienteFácil começou como um cadastro simples de clientes e, nesta sprint, foi evoluído para funcionar como uma aplicação full stack com front-end, API própria, banco local e consumo de uma API externa.

A proposta é ajudar profissionais autônomos a guardar e consultar dados de clientes de forma mais organizada, sem depender de planilhas, papel ou conversas antigas de WhatsApp.

## O que esta API faz

Esta API é responsável por:

- cadastrar clientes;
- listar clientes cadastrados;
- buscar um cliente pelo nome;
- atualizar os dados de um cliente;
- excluir um cliente;
- consultar endereço pelo CEP usando o ViaCEP;
- salvar os dados em um banco SQLite.

## Tecnologias utilizadas

- Python
- Flask
- flask-openapi3
- SQLAlchemy
- SQLite
- Swagger / OpenAPI
- Docker

## Arquitetura da solução

<img width="962" height="467" alt="image" src="https://github.com/user-attachments/assets/3fde8564-fcf4-4b0e-a89c-ee0ac29f0785" />


O fluxo principal é simples:

1. O usuário acessa o front-end pelo navegador.
2. O front-end envia requisições HTTP para a API ClienteFácil.
3. A API grava e consulta os dados no SQLite.
4. Quando necessário, a API consulta o ViaCEP e devolve o endereço para o front-end.

## Como executar localmente

Na pasta da API, crie e ative o ambiente virtual:

```bash
python -m venv venv
venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute a API:

```bash
flask --app app run --host 0.0.0.0 --port 5000
```

Com a API rodando, a documentação Swagger fica disponível em:

```text
http://127.0.0.1:5000/openapi/swagger#/
```

## Como executar com Docker

Na pasta da API, construa a imagem:

```bash
docker build -t clientefacil-api .
```

Depois execute o container:

```bash
docker run -p 5000:5000 clientefacil-api
```

## Rotas principais

| Método | Rota | Função |
|---|---|---|
| GET | `/clientes` | Lista todos os clientes |
| GET | `/cliente?nome=Maria` | Busca um cliente pelo nome |
| POST | `/cliente` | Cadastra um novo cliente |
| PUT | `/cliente` | Atualiza dados de um cliente |
| DELETE | `/cliente?nome=Maria` | Remove um cliente |
| GET | `/endereco?cep=01001000` | Consulta endereço pelo CEP |

## API externa utilizada

Foi utilizado o ViaCEP:

```text
https://viacep.com.br/
```

A rota consultada segue este formato:

```text
https://viacep.com.br/ws/{cep}/json/
```

O ViaCEP é público e não exige cadastro para a consulta usada neste projeto. A API ClienteFácil recebe o CEP, consulta o ViaCEP e devolve para o front-end apenas os dados usados na tela: CEP, logradouro, bairro, cidade e UF.

## Repositórios

- API: https://github.com/alinefreis2024-web/clientefacil-api
- Front-end: https://github.com/alinefreis2024-web/clientefacil-frontend

## Autora

Desenvolvido por Aline Ferreira dos Reis para a Sprint II do MVP da PUC-Rio.
