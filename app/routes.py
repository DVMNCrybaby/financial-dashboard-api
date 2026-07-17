from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.database import SessionLocal
from app import crud, schemas, models
from app.utils.csv_import import importar_csv

router = APIRouter(prefix="/transacoes", tags=["Transações"])

# Database session dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# -------------------------------
# Auxiliary endpoints for data import, summary, and statistics
# -------------------------------

@router.post("/importar_csv")
def importar(file: UploadFile = File(...), db: Session = Depends(get_db)):
    with open("temp.csv", "wb") as f:
        f.write(file.file.read())
    importar_csv("temp.csv", db)
    return {"mensagem": "CSV importado com sucesso!"}

# Tracking income, expenses, and the mystery of where my money disappeared.

@router.get("/resumo")
def resumo(db: Session = Depends(get_db)):
    receitas = (
        db.query(func.sum(models.Transacao.valor))
        .filter(models.Transacao.tipo == "receita")
        .scalar()
    ) or 0
    despesas = (
        db.query(func.sum(models.Transacao.valor))
        .filter(models.Transacao.tipo == "despesa")
        .scalar()
    ) or 0
    saldo = receitas - despesas
    return {"receitas": float(receitas), "despesas": float(despesas), "saldo": float(saldo)}

@router.get("/estatisticas")
def estatisticas(db: Session = Depends(get_db)):
    resultados = (
        db.query(models.Transacao.categoria, func.sum(models.Transacao.valor))
        .group_by(models.Transacao.categoria)
        .all()
    )
    estatisticas = {categoria: float(total) for categoria, total in resultados}
    return {"estatisticas": estatisticas}

# -------------------------------
# CRUD routes
# -------------------------------

@router.post("/", response_model=schemas.Transacao)
def create(transacao: schemas.TransacaoCreate, db: Session = Depends(get_db)):
    return crud.create_transacao(db, transacao)


@router.get("/", response_model=list[schemas.Transacao])
def read(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_transacoes(db, skip, limit)


#ID routes always go at the end, my friendos
@router.get("/{transacao_id}", response_model=schemas.Transacao)
def read_one(transacao_id: int, db: Session = Depends(get_db)):
    return crud.get_transacao(db, transacao_id)


@router.put("/{transacao_id}", response_model=schemas.Transacao)
def update(transacao_id: int, transacao: schemas.TransacaoCreate, db: Session = Depends(get_db)):
    return crud.update_transacao(db, transacao_id, transacao)


@router.delete("/{transacao_id}")
def delete(transacao_id: int, db: Session = Depends(get_db)):
    return crud.delete_transacao(db, transacao_id)