# 🚀 URL Shortener API (FastAPI)

A simple and scalable URL Shortener built using FastAPI, SQLAlchemy, and SQLite.
This project converts long URLs into short links and redirects users efficiently.

---

## 📌 Features

* 🔗 Shorten long URLs
* 🔁 Redirect using short URLs
* ✅ Input validation using Pydantic
* 🗄️ Database storage using SQLite
* ⚡ FastAPI automatic docs (Swagger UI)
* ❌ Handles invalid and missing URLs

---

## 🧱 Tech Stack

* **Backend:** FastAPI
* **Database:** SQLite
* **ORM:** SQLAlchemy
* **Validation:** Pydantic

---

## 📂 Project Structure

```
url_shortener/
│── main.py          # API routes
│── databases.py     # Database connection
│── model.py         # DB models
│── schemas.py       # Request/Response schemas
│── utils.py         # Helper functions
│── urls.db          # SQLite database
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```
git clone <your-repo-link>
cd url_shortener
```

### 2️⃣ Install dependencies

```
pip install fastapi uvicorn sqlalchemy pydantic
```

### 3️⃣ Run the server

```
uvicorn main:app --reload
```

---

## 🌐 API Endpoints

### 🔹 1. Shorten URL

**POST /shorten**

Request:

```json
{
  "original_url": "https://google.com"
}
```

Response:

```json
{
  "short_url": "http://localhost:8000/abc123"
}
```

---

### 🔹 2. Redirect URL

**GET /{short_code}**

Example:

```
http://localhost:8000/abc123
```

👉 Redirects to original URL

---

## 📖 API Documentation

FastAPI provides built-in interactive docs:

* Swagger UI: http://127.0.0.1:8000/docs
* ReDoc: http://127.0.0.1:8000/redoc

---



---

## 🚀 Future Improvements

* 🔥 Add Redis caching for performance
* 📊 Add click analytics
* ⏳ Add URL expiration
* ⚖️ Add rate limiting
* ☁️ Deploy on cloud (Render/AWS)

---

## 🧠 Learnings

* API design using FASTAPI
* Database integration with SQLAlchemy
* Request validation with Pydantic
* System design basics (scalability, caching, etc.)

---

## 👨‍💻 Author

Raghu Narayana

---
