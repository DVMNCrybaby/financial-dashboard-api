import csv
from sqlalchemy.orm import Session
from app import models
from app.database import engine

def importar_csv(caminho_csv: str):
    # Create a database session
    session = Session(bind=engine)

    try:
        with open(caminho_csv, newline='', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                
                usuario = models.Usuario(
                    nome=linha["nome"],
                    email=linha["email"]
                )
                session.add(usuario)

        session.commit()
        print("CSV importado com sucesso!")

    except Exception as e:
        session.rollback()
        print(f"Erro ao importar CSV: {e}")

    finally:
        session.close()