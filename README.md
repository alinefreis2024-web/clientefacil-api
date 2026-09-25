# ClienteFácil API

API desenvolvida para o MVP do Sprint II da pós-graduação em Desenvolvimento Full Stack da PUC-Rio.

## Sobre o projeto

O ClienteFácil nasceu no Sprint I como um cadastro simples de clientes. No Sprint II, o projeto foi evoluído para trabalhar com mais dados do cliente e com consulta de endereço por CEP.

A ideia é ajudar profissionais autônomos que ainda guardam informações de clientes em planilhas, papel ou conversas de WhatsApp. Nesta versão, a API permite cadastrar, consultar, alterar e excluir clientes, salvando os dados em SQLite.

Também foi adicionada uma consulta ao ViaCEP para preencher endereço a partir do CEP informado.

## Tecnologias utilizadas

- Python
- Flask
- Flask-OpenAPI3
- SQLAlchemy
- SQLite
- Swagger
- Docker

## Execução local

Na pasta do projeto, crie o ambiente virtual:

```bash
python -m venv venv
```

Ative o ambiente no Windows:

```bash
venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Depois execute a API:

```bash
flask run --host 0.0.0.0 --port 5000
```

Com a API rodando, a documentação Swagger fica disponível em:

<http://127.0.0.1:5000/openapi/>

## Execução com Docker

Na pasta da API, execute:

```bash
docker build -t clientefacil-api .
```

Depois rode o container:

```bash
docker run -p 5000:5000 clientefacil-api
```

## Rotas da API

- `GET /clientes`: lista todos os clientes.
- `GET /cliente?nome=Maria`: busca um cliente cadastrado pelo nome.
- `POST /cliente`: cadastra um cliente.
- `PUT /cliente`: atualiza os dados do cliente.
- `DELETE /cliente?nome=Maria`: remove um cliente.
- `GET /endereco?cep=01001000`: consulta endereço usando o ViaCEP.

## Uso da API externa

Para atender ao requisito de uso de uma API externa, foi utilizado o ViaCEP:

<https://viacep.com.br/>

Exemplo de rota usada pela aplicação:

```text
https://viacep.com.br/ws/{cep}/json/
```

O ViaCEP é público e não exige cadastro para a consulta básica usada neste projeto. A API ClienteFácil recebe o CEP, consulta o ViaCEP e devolve para o front-end somente os campos usados na tela: CEP, logradouro, bairro, cidade e UF.

## Cenário adotado

O cenário escolhido foi o de uma interface web consumindo uma API própria. A API própria salva os dados no SQLite e também faz a consulta ao serviço externo ViaCEP.

Na prática, o fluxo ficou assim: o usuário usa o front-end, o front-end chama a API ClienteFácil, e a API acessa o banco SQLite. Quando o usuário informa um CEP, a API também consulta o ViaCEP para buscar o endereço.

## Autor

Desenvolvido por **Aline Ferreira dos Reis**.

- GitHub: <https://github.com/alinefreis2024-web>
