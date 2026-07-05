# ClienteFácil API

API desenvolvida para a Sprint 1 do MVP da disciplina Desenvolvimento Full Stack do MBA PUC-Rio.

## Sobre o projeto

O ClienteFácil é um sistema para ajudar profissionais autônomos a organizar os dados dos seus clientes.

## Problema

Muitos profissionais autônomos ainda guardam informações dos clientes em papel, planilhas ou conversas de WhatsApp. Isso pode dificultar a organização e a consulta dessas informações.

O ClienteFácil foi criado para ajudar estes profissionais a centralizar essas informações de forma simples utilizando uma API integrada a um banco de dados SQLite.

## Funcionalidades

### O que o sistema faz?

Nesta primeira versão, a API permite:
*cadastrar clientes;
*listar todos clientes;
*buscar um cliente pelo nome;
*excluir um cliente.

## Tecnologias utilizadas

- Python
- Flask
- Flask-OpenAPI3
- SQLAlchemy
- SQLite
- Swagger (OpenAPI)

## Como executar

1.Criar o ambiente virtual:

```bash
python -m venv venv
```

2.Ativar o ambiente virtual.

Windows:

```bash
venv\Scripts\activate
```

3.Instalar as dependências:

```bash
pip install -r requirements.txt
```

4.Executar a aplicação:

```bash
python app.py
```

## Documentação da API

Após iniciar a aplicação, acesse:

```http://127.0.0.1:5000/openapi/swagger
```

## Autor

Desenvolvido por **Aline Ferreira dos Reis**.

- GitHub: <https://github.com/alinefreis2024-web>
