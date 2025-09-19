# 🌐 AWS Translation Service

This project is a **FastAPI web application** that takes user input (Name & Address in English), **translates it into Kannada using AWS Translate**, and stores both English and Kannada data into a **database (SQLite/MySQL with SQLAlchemy ORM)**.

---

## 🚀 Features

* FastAPI backend with Jinja2 templates for frontend form
* Real-time translation (English ➞ Kannada) via **AWS Translate API**
* Data persistence with **SQLAlchemy ORM**
* HTML form submission with automatic storage of both English & Kannada text
* REST API endpoint for translation

---

## 📂 Project Structure

```
AWS-Translation-Service/
├── main.py              # FastAPI application entry
├── models.py            # SQLAlchemy models
├── transelate.py        # AWS Translate function
├── database.py          # Database connection & SessionLocal
├── templates/
│   └── formaws.html     # HTML form page
└── README.md            # Project documentation
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone <your-repo-url>
cd AWS-Translation-Service
```

### 2️⃣ Create Virtual Environment & Install Dependencies

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

pip install fastapi uvicorn sqlalchemy pydantic jinja2 boto3
```

### 3️⃣ Configure AWS Credentials

Make sure you have an IAM User with `TranslateFullAccess` or equivalent permissions.
Run:

```bash
aws configure
```

Provide:

* AWS Access Key ID
* AWS Secret Access Key
* Default region → `ap-south-1`

### 4️⃣ Run Database Migrations

Database tables are auto-created using:

```python
Base.metadata.create_all(bind=engine)
```

(See `database.py` for engine configuration, SQLite/MySQL supported)

### 5️⃣ Start FastAPI Server

```bash
uvicorn main:app --reload
```

Now visit 👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📱 API Endpoints

### Form Page

```
GET /
```

Renders the HTML form.

### Submit Form

```
POST /submit
```

Stores English & Kannada name/address in the database.

### Translate Text

```
POST /transliterate
```

Request Body:

```json
{
  "text": "Hello World",
  "method": "aws"
}
```

Response:

```json
{
  "translated": "ಹಲೋ ವರ್ಲ್ಡ್"
}
```

---

## 🗂️ Database (UserData Table)

| id | name\_en | name\_kn | address\_en | address\_kn         |
| -- | -------- | -------- | ----------- | ------------------- |
| 1  | John Doe | ಜಾನ್ ಡೋ  | MG Road BLR | ಎಂಜಿ ರಸ್ತೆ ಬೆಂಗಳೂರು |

---

## 📌 Requirements

* Python 3.8+
* AWS Translate enabled in your AWS account
* FastAPI + Uvicorn
* SQLAlchemy ORM
* boto3
