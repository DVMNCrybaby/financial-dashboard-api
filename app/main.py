from fastapi import FastAPI
from app.routes import router as transacoes_router
from app.database import engine, Base
from app import models
from app.utils.csv_import import importar_csv

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Dashboard Financeiro API")

app.include_router(transacoes_router)

@app.get("/")
def home():
    return {"mensagem": "Minha API está funcionando!"}