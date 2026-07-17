from sqlalchemy.orm import Session
from app import models, schemas

def create_transacao(db: Session, transacao: schemas.TransacaoCreate):
    db_transacao = models.Transacao(**transacao.dict())
    db.add(db_transacao)
    db.commit()
    db.refresh(db_transacao)
    return db_transacao

def get_transacoes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Transacao).offset(skip).limit(limit).all()

def get_transacao(db: Session, transacao_id: int):
    return db.query(models.Transacao).filter(models.Transacao.id == transacao_id).first()

def update_transacao(db: Session, transacao_id: int, transacao: schemas.TransacaoCreate):
    db_transacao = get_transacao(db, transacao_id)
    if db_transacao:
        for key, value in transacao.dict().items():
            setattr(db_transacao, key, value)
        db.commit()
        db.refresh(db_transacao)
    return db_transacao

def delete_transacao(db: Session, transacao_id: int):
    db_transacao = get_transacao(db, transacao_id)
    if db_transacao:
        db.delete(db_transacao)
        db.commit()
    return db_transacao