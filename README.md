# 📊 Financial Dashboard API

API REST desenvolvida com **FastAPI** para gerenciamento e análise de transações financeiras.

A aplicação realiza a importação de dados por meio de arquivos CSV, armazena as informações em um banco de dados MySQL e disponibiliza indicadores consolidados para consumo por dashboards, ferramentas de Business Intelligence (BI) ou outras aplicações.

---

## 🚀 Tecnologias utilizadas

- Python 3.13
- FastAPI
- SQLAlchemy
- MySQL 8
- Docker
- Docker Compose
- Pydantic

---

## 📌 Funcionalidades

- Importação de transações via CSV
- CRUD completo de transações
- Resumo financeiro
  - Total de receitas
  - Total de despesas
  - Saldo
- Estatísticas por categoria
- Persistência em banco de dados MySQL
- API preparada para integração com dashboards e ferramentas de BI

---

## 📂 Estrutura do projeto

```text
backend/
│
├── app/
│   ├── main.py
│   ├── routes.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── database.py
│   └── utils/
│       └── csv_import.py
│
├── Dockerfile
├── requirements.txt
└── .gitignore
```

---

## 📈 Fluxo da aplicação

```text
Arquivo CSV
      │
      ▼
Importação dos dados
      │
      ▼
Tratamento e validação
      │
      ▼
Banco de dados MySQL
      │
      ▼
API FastAPI
      │
      ▼
Resumo financeiro e estatísticas
      │
      ▼
Dashboards / Business Intelligence
```

---

## 📡 Endpoints

### Importar CSV

```http
POST /transacoes/importar_csv
```

Importa um arquivo CSV contendo as transações financeiras.

---

### Listar transações

```http
GET /transacoes
```

---

### Buscar transação

```http
GET /transacoes/{id}
```

---

### Criar transação

```http
POST /transacoes
```

---

### Atualizar transação

```http
PUT /transacoes/{id}
```

---

### Remover transação

```http
DELETE /transacoes/{id}
```

---

### Resumo financeiro

```http
GET /transacoes/resumo
```

Exemplo de resposta:

```json
{
  "receitas": 8500,
  "despesas": 4200,
  "saldo": 4300
}
```

---

### Estatísticas por categoria

```http
GET /transacoes/estatisticas
```

Exemplo de resposta:

```json
{
  "estatisticas": {
    "Alimentação": 950,
    "Transporte": 520,
    "Moradia": 1800
  }
}
```

---

## 🐳 Executando com Docker

```bash
docker compose up --build
```

A aplicação ficará disponível em:

```text
http://localhost:8000
```

---

## 💻 Executando localmente

Instale as dependências:

```bash
pip install -r requirements.txt
```

Inicie a API:

```bash
uvicorn app.main:app --reload
```

---

## 🎯 Sobre o projeto

Este projeto foi desenvolvido para oferecer uma solução simples de gerenciamento e análise de dados financeiros.

A API permite importar transações por meio de arquivos CSV, armazenar os dados em um banco relacional e disponibilizar informações consolidadas, como resumo financeiro e estatísticas por categoria, facilitando a integração com dashboards e ferramentas de Business Intelligence.

Durante o desenvolvimento foram aplicados conceitos de:

- Desenvolvimento de APIs REST com FastAPI;
- Modelagem de banco de dados relacional;
- SQLAlchemy ORM;
- Importação e tratamento de dados;
- Operações CRUD;
- Consultas agregadas;
- Containerização com Docker.

---

## 🔮 Melhorias futuras

- Autenticação com JWT
- Paginação e filtros
- Testes automatizados
- Dashboard web para visualização dos indicadores
- Deploy em ambiente de produção
- Documentação mais detalhada da API

---

## 👨‍💻 Autor

**João Pedro Colares Kretli**

GitHub: https://github.com/DVMNCrybaby
