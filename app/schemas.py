from pydantic import BaseModel
from datetime import date
#just basics
class TransacaoBase(BaseModel):
    data: date
    descricao: str
    valor: float
    categoria: str
    tipo: str

class TransacaoCreate(TransacaoBase):
    pass

class Transacao(TransacaoBase):
    id: int

    class Config:
        from_attributes = True