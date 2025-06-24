# 🌙 Late Show API - Phase 4 Code Challenge

A Flask REST API for managing a Late Night TV Show's episodes, guests, and appearances, with JWT-based authentication, PostgreSQL integration, and Postman for API testing.

---

## 📁 Folder Structure
```
.
├── server/
│ ├── app.py
│ ├── config.py
│ ├── seed.py
│ ├── models/
│ │ ├── init.py
│ │ ├── guest.py
│ │ ├── episode.py
│ │ ├── appearance.py
│ │ └── user.py
│ ├── controllers/
│ │ ├── init.py
│ │ ├── guest_controller.py
│ │ ├── episode_controller.py
│ │ ├── appearance_controller.py
│ │ └── auth_controller.py
├── migrations/
├── challenge-4-lateshow.postman_collection.json
└── README.md
```

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```
git clone https://github.com/<your-username>/late-show-api.git
cd late-show-api
```
### 2. Install Dependencies
```
pipenv install 
pipenv shell
```
### 3. PostgreSQL Configuration
Create a PostgreSQL database named:
```
CREATE DATABASE late_show_db;
```
Set your database URI and env variables in .env:
```
FLASK_APP=server/app.py
FLASK_RUN_PORT=5555
FLASK_SQLALCHEMY_DATABASE_URI = postgresql://<your-username>:<your-password>@localhost:5432/late_show_db
FLASK_JWT_SECRET_KEY=super-secret
<!-- Change the secret key -->
```
### 4. Initialise Database and seed
```
flask db upgrade
python -m server.seed
```

## Authentication Flow
### Register

POST /register
```
{
  "username": "admin",
  "password": "adminpass"
}
```
### Login

POST /login
```
{
  "username": "admin",
  "password": "adminpass"
}
```
Response:
```
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGci..."
}
```
Use the returned token in headers for protected routes:

Authorization: Bearer <token>

## Routes
Endpoint	Method	Auth Required	Description

| Route                    | Method | Auth Required  | Description                          |
|--------------------------|--------|----------------|--------------------------------------|
| `/register`              | POST   | ❌             | Register a new user                  |
| `/login`                 | POST   | ❌             | Log in and receive JWT token         |
| `/episodes`              | GET    | ❌             | List all episodes                    |
| `/episodes/<int:id>`     | GET    | ❌             | Get specific episode and appearances |
| `/episodes/<int:id>`     | DELETE | ✅             | Delete episode (and appearances)     |
| `/guests`                | GET    | ❌             | List all guests                      |
| `/appearances`           | POST   | ✅             | Create a new appearance              |


## Postman Testing
Steps:

1. Import challenge-4-lateshow.postman_collection.json into Postman.
2. Test the following flows:

    - Register a user
    - Login and retrieve token
    - Use Bearer <token> in Authorization header for protected routes
    - Create appearances and delete episodes

3. Use correct request formats as defined above.