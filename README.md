# 📝 Note Taking Backend API

A RESTful Note Taking Backend built with **FastAPI**, **PostgreSQL**, and **Tortoise ORM**. The application provides secure user authentication using **JWT** and allows authenticated users to perform CRUD operations on their personal notes.

---

## 🛠️ Tech Stack

- **Backend:** FastAPI
- **Database:** PostgreSQL
- **ORM:** Tortoise ORM
- **Authentication:** JWT (python-jose)
- **Password Hashing:** Passlib + Bcrypt
- **Database Driver:** asyncpg
- **Migration Tool:** Aerich
- **Validation:** Pydantic

---

## 📂 Project Structure

```text
app/
│
├── core/
│   ├── config.py
│   ├── database.py
│   └── security.py
│
├── dependencies/
│   └── auth.py
│
├── models/
│   ├── user.py
│   └── note.py
│
├── routers/
│   ├── auth.py
│   ├── home.py
│   └── notes.py
│
├── schemas/
│   ├── auth.py
│   ├── user.py
│   └── note.py
│
├── services/
│   ├── auth_service.py
│   └── note_service.py
│
└── main.py
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/SuyashProc/note-taking-backend.git
cd note-taking-backend
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Database Migrations

```bash
aerich upgrade
```

---

### 6. Run the Server

```bash
uvicorn app.main:app --reload
```

The application will be available at

```
http://127.0.0.1:8000
```

Interactive API Documentation

```
http://127.0.0.1:8000/docs
```

---

## 🔐 Authentication

The API uses JWT Authentication.

1. Register a new user.
2. Login using your username and password.
3. Copy the generated access token.
4. Click **Authorize** in Swagger UI.
5. Authenticate using the token.
6. Access protected endpoints.

---

## 📌 API Endpoints

### Authentication

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/auth/signup` | Register a new user |
| POST | `/auth/login` | Login and receive JWT |

---

### Notes

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/notes` | Create a note |
| GET | `/notes` | Get all notes |
| GET | `/notes/{note_id}` | Get a specific note |
| PUT | `/notes/{note_id}` | Update a note |
| DELETE | `/notes/{note_id}` | Delete a note |

---

## 🧠 Key Concepts Implemented

- FastAPI Dependency Injection
- JWT Authentication
- OAuth2 Password Flow
- Service Layer Architecture
- CRUD Operations
- ORM Relationships
- Request Validation with Pydantic
- Authorization using JWT
- Environment Variable Management

---

## 📸 API Documentation

FastAPI automatically generates interactive Swagger documentation.

```
http://127.0.0.1:8000/docs

## 👨‍💻 Author

**Suyash Singh**

