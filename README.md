# async-data-processing-api
High-performance FastAPI &amp; Pandas Data Ingestion, Cleaning &amp; SQL Storage API

# ⚡ Async Data Ingestion & Analytics Engine (FastAPI + Pandas + SQL)

A high-performance, asynchronous RESTful API designed for automated data ingestion, cleaning, transformation using **Pandas**, and relational storage via **SQLAlchemy (SQL Databases)**.

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=flat-square&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688?style=flat-square&logo=fastapi)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=flat-square&logo=pandas)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red?style=flat-square)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=flat-square&logo=docker)

---

## 🛠️ Tech Stack & Core Technologies

- **Language:** Python 3.11+
- **Framework:** FastAPI (Asynchronous Endpoints & OpenAPI / Swagger Docs)
- **Data Engineering:** Pandas & NumPy (Data Sanitization, Ingestion, Deduplication, Transformation)
- **Database Layer:** SQLAlchemy ORM, PostgreSQL, MySQL
- **Containerization & DevOps:** Docker, Docker Compose

---

## 🔥 Key Features

- **High-Speed File Processing:** Ingest and parse bulk dataset uploads (CSV, Excel) in real-time.
- **Automated Pandas Data Pipeline:** Handles deduplication, NULL value sanitization, type coercion, and metric calculations.
- **Optimized SQL Integration:** Bulk insert mappings into SQL databases using SQLAlchemy.
- **Interactive Swagger Documentation:** Built-in UI testing interface via OpenAPI specifications.
- **Production Containerized:** Fully packaged with Docker and Docker-Compose for instant deployment.

---

## 📂 Project Structure

```text
async-data-processing-api/
│
├── app/
│   ├── main.py            # Main FastAPI Engine & Endpoints
│   └── services.py        # Pandas Data Pipeline & Cleaning Engine
│
├── Dockerfile             # Container setup
├── requirements.txt       # Python Dependencies
└── README.md              # Project Documentation
```

# Clone the Repository
git clone [https://github.com/muhammadyasir119/async-data-processing-api.git](https://github.com/muhammadyasir119/async-data-processing-api.git)

# Navigate into project directory
cd async-data-processing-api

# Build & Run with Docker
docker build -t async-data-api .
docker run -p 8000:8000 async-data-api
## Upwork
https://www.upwork.com/freelancers/~01b60353c6f1506287?mp_source=share
