from sqlalchemy import Column, String, Integer

from model import Base


class Cliente(Base):
    __tablename__ = "cliente"

    id = Column("pk_cliente", Integer, primary_key=True)
    nome = Column(String(140), unique=True)
    telefone = Column(String(20))
    email = Column(String(100))
    cep = Column(String(9))
    logradouro = Column(String(140))
    bairro = Column(String(100))
    cidade = Column(String(100))
    uf = Column(String(2))
    

    def __init__(
        self,
        nome: str, 
        telefone: str,
        email: str,
        cep: str = "",
        logradouro: str = "",
        bairro: str = "",
        cidade: str = "",
        uf: str = "",
        
    ):
        """
        Cria um novo cliente.

        Argumentos:
            nome: Nome do cliente.
            telefone: Telefone do cliente.
            email: Email do cliente.
            cep: CEP do cliente.
            logradouro: Rua ou avenida do cliente.
            bairro: Bairro do cliente.
            cidade: Cidade do cliente.
            uf: Estado do cliente.
        """ 
        
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.cep = cep
        self.logradouro = logradouro
        self.bairro = bairro
        self.cidade = cidade
        self.uf = uf
