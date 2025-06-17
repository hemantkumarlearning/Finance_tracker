# Finance Tracker API

A simple and secure Finance Tracker API built using Django REST Framework and JWT authentication. Users can register, authenticate, and manage their financial activities like transactions, budgets, and categories. The API also provides monthly financial reports.

---

## Features

- User Registration & JWT Authentication
- Category Management (Add/Edit/Delete)
- Transaction Management (Add/Edit/Delete)
- Budget Management
- Monthly Financial Report Summary

---

## Tech Stack

- **Backend**: Django, Django REST Framework
- **Authentication**: JSON Web Tokens (JWT)
- **Database**: SQLite (default), can be swapped with PostgreSQL or others

---

## Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/finance-tracker-api.git
cd finance-tracker-api
```

### 2. Create & Activate Virtual Environment

```
python -m venv env
On Windows: env\Scripts\activate
````

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Run Migrations

```
python manage.py migrate
```


### 5. Run the Server

```
python manage.py runserver
```

## Authentication

This API uses JWT for authentication.

- Register: POST /api/users/register/

- Login: POST /api/token/ → returns access and refresh tokens

- Refresh Token: POST /api/token/refresh/

Attach the access token to the Authorization header:

```
Authorization: Bearer <your_token>
```

## API Endpoints

All endpoints require JWT auth unless mentioned otherwise.

#### User

- POST /api/users/register/ – Register new user

- POST /api/token/ – Login (JWT)

#### Categories

- GET /api/categories/

- POST /api/categories/

- PUT /api/categories/<id>/

- DELETE /api/categories/<id>/

#### Transactions

- GET /api/transactions/

- POST /api/transactions/

- PUT /api/transactions/<id>/

- DELETE /api/transactions/<id>/

#### Budgets

- GET /api/budgets/

- POST /api/budgets/

- PUT /api/budgets/<id>/

- DELETE /api/budgets/<id>/

#### Monthly Report

- GET /api/reports/monthly/?month=<year>-<month> – View monthly summary


### Monthly Report

The report includes:

- Total income

- Total expenses

- Budget vs Actual comparison

- Breakdown by category

