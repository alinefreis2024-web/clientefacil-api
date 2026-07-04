# Importações
from pydantic import BaseModel
from typing import List
from model.cliente import Cliente


class ClienteSchema(BaseModel):
    """Modelo de cadastro de cliente."""
    
    nome: str = "Maria da Silva"
    telefone: str = "11999999999"
    email: str = "maria@gmail.com"
   

class ClienteBuscaSchema(BaseModel):
    """Modelo para buscar clientes."""

    nome: str = "Maria da Silva"


class ClienteViewSchema(BaseModel):
    """Modelo para mostrar um cliente."""

    id: int = 1
    nome: str = "Maria da Silva"
    telefone: str = "11999999999"
    email: str = "maria@gmail.com"


class ListagemClientesSchema(BaseModel):
    """Modelo para listar clientes."""

    clientes: List[ClienteViewSchema] 


class ClienteDeleteSchema(BaseModel):
    """Modelo de resposta após excluir um cliente."""

    mensagem: str = "Cliente deletado com sucesso."
    nome: str = "Maria da Silva"


def apresenta_cliente(cliente: Cliente):
    """Retorna os dados do cliente."""

    return {
        "id": cliente.id,  
        "nome": cliente.nome,
        "telefone": cliente.telefone,
        "email": cliente.email,
    }


def apresenta_clientes(clientes: List[Cliente]):
    """Retorna uma lista de clientes para resposta da API."""

    resultado = []

    for cliente in clientes:
        resultado.append({
            "id": cliente.id,
            "nome": cliente.nome,
            "telefone": cliente.telefone,
            "email": cliente.email,
        })

    return {"clientes": resultado}
