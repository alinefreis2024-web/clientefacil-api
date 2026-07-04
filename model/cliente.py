from sqlalchemy import Column, String, Integer

from model import Base


class Cliente(Base):
    __tablename__ = "cliente"

    id = Column("pk_cliente", Integer, primary_key=True)
    nome = Column(String(140), unique=True)
    telefone = Column(String(20))
    email = Column(String(100))
    

    def __init__(
        self,
        nome: str, 
        telefone: str,
        email: str,
        
    ):
        """
        Cria um novo cliente.

        Argumentos:
            nome: Nome do cliente.
            telefone: Telefone do cliente.
            email: Email do cliente.
        """ 
        
        self.nome = nome
        self.telefone = telefone
        self.email = email