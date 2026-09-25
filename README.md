# ClienteFácil API

API desenvolvida para o Sprint II do MVP da disciplina Desenvolvimento Full Stack do MBA PUC-Rio.

## Sobre o projeto

O ClienteFácil é um sistema para ajudar profissionais autônomos a organizar os dados dos seus clientes.

Nesta versão, a API permite cadastrar, listar, buscar, atualizar e excluir clientes. Também consulta a API pública ViaCEP para buscar endereço pelo CEP informado.

## Tecnologias utilizadas

- Python
- Flask
- Flask-OpenAPI3
- SQLAlchemy
- SQLite
- Swagger
- Docker

## Como executar localmente

1. Criar o ambiente virtual:

```bash
python -m venv venv
```

2. Ativar o ambiente virtual no Windows:

```bash
venv\Scripts\activate
```

3. Instalar as dependências:

```bash
pip install -r requirements.txt
```

4. Executar a aplicação:

```bash
flask run --host 0.0.0.0 --port 5000
```

## Como executar com Docker

1. Construir a imagem:

```bash
docker build -t clientefacil-api .
```

2. Executar o container:

```bash
docker run -p 5000:5000 clientefacil-api
```

## Documentação Swagger

Após iniciar a aplicação, acesse:

<http://127.0.0.1:5000/openapi/>

## Rotas principais

- `GET /clientes`: lista todos os clientes.
- `GET /cliente?nome=Maria`: busca um cliente pelo nome.
- `POST /cliente`: cadastra um cliente.
- `PUT /cliente`: atualiza os dados de um cliente.
- `DELETE /cliente?nome=Maria`: remove um cliente.
- `GET /endereco?cep=01001000`: consulta endereço pelo CEP.

## API externa utilizada

Foi utilizada a API pública ViaCEP:

<https://viacep.com.br/>

Rota utilizada:

```text
https://viacep.com.br/ws/{cep}/json/
```

A API não exige cadastro para uso básico. Os dados retornados são tratados pela API ClienteFácil antes de serem enviados ao front-end.

## Arquitetura

```text
Usuário
  |
  v
Front-end ClienteFácil
  |
  v
API ClienteFácil
  |
  v
Banco SQLite

API ClienteFácil
  |
  v
API externa ViaCEP
```

## Autor

Desenvolvido por **Aline Ferreira dos Reis**.

- GitHub: <https://github.com/alinefreis2024-web>
