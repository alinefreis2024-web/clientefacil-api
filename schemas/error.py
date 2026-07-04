from pydantic import BaseModel


class ErrorSchema(BaseModel):
   """Modelo de resposta de erro."""
 
   mensagem: str = "Erro ao processar a solicitação."