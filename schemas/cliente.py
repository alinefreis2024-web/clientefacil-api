# Importações
from pydantic import BaseModel
from typing import List
from model.cliente import Cliente


class ClienteSchema(BaseModel):
    """Modelo de cadastro de cliente."""
    
    nome: str = "Maria da Silva"
    telefone: str = "11999999999"
    email: str = "maria@gmail.com"
    cep: str = "01001-000"
    logradouro: str = "Praça da Sé"
    bairro: str = "Sé"
    cidade: str = "São Paulo"
    uf: str = "SP"
   

class ClienteBuscaSchema(BaseModel):
    """Modelo para buscar clientes."""

    nome: str = "Maria da Silva"


class ClienteAtualizaSchema(BaseModel):
    """Modelo para atualizar clientes."""

    nome: str = "Maria da Silva"
    telefone: str = "11888888888"
    email: str = "maria.atualizada@gmail.com"
    cep: str = "01001-000"
    logradouro: str = "Praça da Sé"
    bairro: str = "Sé"
    cidade: str = "São Paulo"
    uf: str = "SP"


class CepBuscaSchema(BaseModel):
    """Modelo para buscar endereço pelo CEP."""

    cep: str = "01001000"


class EnderecoViewSchema(BaseModel):
    """Modelo para mostrar endereço retornado pelo ViaCEP."""

    cep: str = "01001-000"
    logradouro: str = "Praça da Sé"
    bairro: str = "Sé"
    cidade: str = "São Paulo"
    uf: str = "SP"


class ClienteViewSchema(BaseModel):
    """Modelo para mostrar um cliente."""

    id: int = 1
    nome: str = "Maria da Silva"
    telefone: str = "11999999999"
    email: str = "maria@gmail.com"
    cep: str = "01001-000"
    logradouro: str = "Praça da Sé"
    bairro: str = "Sé"
    cidade: str = "São Paulo"
    uf: str = "SP"


class ListagemClientesSchema(BaseModel):
    """Modelo para listar clientes."""

    clientes: List[ClienteViewSchema] 


class ClienteDeleteSchema(BaseModel):
    """Modelo de resposta após excluir um cliente."""

    mensagem: str = "Cliente removidi com sucesso."
    nome: str = "Maria da Silva"


def apresenta_cliente(cliente: Cliente):
    """Retorna os dados do cliente."""

    return {
        "id": cliente.id,  
        "nome": cliente.nome,
        "telefone": cliente.telefone,
        "email": cliente.email,
        "cep": cliente.cep,
        "logradouro": cliente.logradouro,
        "bairro": cliente.bairro,
        "cidade": cliente.cidade,
        "uf": cliente.uf,
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
            "cep": cliente.cep,
            "logradouro": cliente.logradouro,
            "bairro": cliente.bairro,
            "cidade": cliente.cidade,
            "uf": cliente.uf,
        })

    return {"clientes": resultado}
