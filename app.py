from flask import redirect
from flask_openapi3 import OpenAPI, Info, Tag
from flask_cors import CORS

from sqlalchemy.exc import IntegrityError

from model import Session
from model.cliente import Cliente

from logger import logger

from schemas import (
    ClienteSchema,
    ClienteBuscaSchema,
    ClienteViewSchema,
    ListagemClientesSchema,
    ClienteDeleteSchema,
    apresenta_cliente,
    apresenta_clientes,
    ErrorSchema,
)

info = Info(
    title="ClienteFácil API", 
    version="1.0.0"
)

app = OpenAPI(__name__, info=info)
CORS(app)

cliente_tag = Tag(name="Cliente", description="Cadastro, listagem, busca e remoção de clientes")


@app.get("/")
def home():
    """Redireciona para Swagger """
    return redirect("/openapi")


@app.post(
    "/cliente",
    tags=[cliente_tag],
    responses={
        "200": ClienteViewSchema,
        "409": ErrorSchema,
        "400": ErrorSchema,
    }
)
def add_cliente(form: ClienteSchema):
    """Adiciona um novo cliente."""

    cliente = Cliente(
        nome=form.nome,
        telefone=form.telefone,
        email=form.email,
    )

    logger.info(f"Adicionando cliente: {cliente.nome}") 

    try:
        session = Session()
        session.add(cliente)
        session.commit()

        logger.info(f"Cliente adicionado com sucesso: {cliente.nome}")
        return apresenta_cliente(cliente), 200

    except IntegrityError:
        error_msg = "Cliente com o mesmo nome já existe."
        logger.warning(error_msg)
        return {"mensagem": error_msg}, 409

    except Exception as e:
        error_msg = "Não foi possível adicionar o cliente."
        logger.warning(f"Erro ao adicionar cliente: {e}")
        return {"mensagem": error_msg}, 400
    

@app.get(
    "/clientes",
    tags=[cliente_tag],
    responses={
        "200": ListagemClientesSchema,
    }
)
def get_clientes():
    """Lista todos os clientes."""

    logger.info("Buscando todos os clientes.")

    session = Session()
    clientes = session.query(Cliente).all()

    return apresenta_clientes(clientes), 200
        
            
@app.get(
    "/cliente",
    tags=[cliente_tag],
    responses={
        "200": ClienteViewSchema,
        "404": ErrorSchema,
    },
)
def get_cliente(query: ClienteBuscaSchema):
    """Busca um cliente pelo nome."""

    nome = query.nome
    logger.info(f"Buscando cliente: {nome}")

    session = Session()
    cliente = session.query(Cliente).filter(Cliente.nome == nome).first()

    if not cliente:
        error_msg = "Cliente não encontrado."
        logger.warning(error_msg)
        return {"mensagem": error_msg}, 404
        
    logger.info(f"Cliente encontrado: {cliente.nome}")
    return apresenta_cliente(cliente), 200


@app.delete(
    "/cliente",
    tags=[cliente_tag],
    responses={
        "200": ClienteDeleteSchema,
        "404": ErrorSchema,
    },
)
def delete_cliente(query: ClienteBuscaSchema):
    """Remove um cliente pelo nome."""

    nome = query.nome
    logger.info(f"Deletando cliente: {nome}")

    session = Session()
    count = session.query(Cliente).filter(Cliente.nome == nome).delete()
    session.commit()
               
    if count:
        logger.info("Cliente removido com sucesso.")
        return {
            "mensagem": "Cliente removido com sucesso.", 
            "nome": nome,
        }, 200
        
    error_msg = "Cliente não encontrado."
    logger.warning(error_msg)
    return {"mensagem": error_msg}, 404
    
    
if __name__ == "__main__":
    app.run(debug=True)
        