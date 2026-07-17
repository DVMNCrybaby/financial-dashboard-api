from sqlalchemy import Column, Integer, String, Float, Date

from app.database import Base


class Transacao(Base):
    __tablename__ = "transacoes"

    id = Column(Integer, primary_key=True, index=True)
    data = Column(Date)
    descricao = Column(String(255))
    valor = Column(Float)
    categoria = Column(String(100))
    tipo = Column(String(20))