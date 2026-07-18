# 📊 Financial Dashboard API

A REST API built with **FastAPI** for managing and analyzing financial transactions.

The application imports transaction data from CSV files, stores it in a MySQL database, and provides summarized financial information for dashboards, Business Intelligence (BI) tools, or other applications.

---

## 🚀 Technologies

- Python 3.13
- FastAPI
- SQLAlchemy
- MySQL 8
- Docker
- Docker Compose
- Pydantic

---

## 📌 Features

- Import financial transactions from CSV files
- Full CRUD operations
- Financial summary
  - Total income
  - Total expenses
  - Current balance
- Statistics grouped by category
- MySQL data persistence
- Ready for integration with dashboards and BI tools

---

## 📂 Project Structure

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

## 📈 Application Flow

```text
CSV File
    │
    ▼
Data Import
    │
    ▼
Data Processing
    │
    ▼
MySQL Database
    │
    ▼
FastAPI
    │
    ▼
Financial Summary & Statistics
    │
    ▼
Dashboard / Business Intelligence
```

---

## 📡 API Endpoints

### Import CSV

```http
POST /transacoes/importar_csv
```

Uploads and imports financial transactions from a CSV file.

---

### List Transactions

```http
GET /transacoes
```

---

### Get Transaction

```http
GET /transacoes/{id}
```

---

### Create Transaction

```http
POST /transacoes
```

---

### Update Transaction

```http
PUT /transacoes/{id}
```

---

### Delete Transaction

```http
DELETE /transacoes/{id}
```

---

### Financial Summary

```http
GET /transacoes/resumo
```

Example response:

```json
{
    "receitas": 8500,
    "despesas": 4200,
    "saldo": 4300
}
```

---

### Category Statistics

```http
GET /transacoes/estatisticas
```

Example response:

```json
{
    "estatisticas": {
        "Food": 950,
        "Transportation": 520,
        "Housing": 1800
    }
}
```

---

## 🐳 Running with Docker

Build and start the containers:

```bash
docker compose up --build
```

The API will be available at:

```text
http://localhost:8000
```

---

## 💻 Running Locally

Install the dependencies:

```bash
pip install -r requirements.txt
```

Start the application:

```bash
uvicorn app.main:app --reload
```

---

## 🎯 About the Project

Financial Dashboard API was developed to provide a simple solution for storing and analyzing financial data.

The application imports transactions from CSV files, stores them in a relational database, and exposes summarized financial information such as income, expenses, balance, and category statistics through a REST API.

This project demonstrates practical knowledge of:

- REST API development with FastAPI
- SQLAlchemy ORM
- Relational database modeling
- CSV data import and processing
- CRUD operations
- Aggregate SQL queries
- Docker containerization

---

## 🔮 Future Improvements

- JWT Authentication
- Pagination and filtering
- Automated tests
- Web dashboard
- Cloud deployment
- Complete API documentation

---

## 👨‍💻 Author

**João Pedro Colares Kretli**

GitHub: https://github.com/DVMNCrybaby
