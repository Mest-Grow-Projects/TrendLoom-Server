# TrendLoom-Server

**TrendLoom-Server** is a robust **E-commerce backend application** built with [FastAPI](https://fastapi.tiangolo.com/), [Beanie ODM](https://beanie-odm.dev/), [Pydantic](https://docs.pydantic.dev/), and [MongoDB](https://www.mongodb.com/).
It provides APIs for **authentication, user management, and product management** in a scalable and secure architecture.

---

## 🌐 Deployed Server

* **Base URL**: [https://trendloom-server.onrender.com](https://trendloom-server.onrender.com)
* **Swagger Docs**: [https://trendloom-server.onrender.com/docs](https://trendloom-server.onrender.com/docs)
* **ReDoc**: [https://trendloom-server.onrender.com/redoc](https://trendloom-server.onrender.com/redoc)


## 🚀 Features

* **Authentication & Authorization**
  * User registration & login
  * JWT-based authentication
  * Email verification & account activation
  * Role-based access (`CUSTOMER`, `ADMIN`, `PRODUCT_ADMIN`)

* **User Management**
  * Manage user profiles
  * Role assignments
  * Account verification and status (`PENDING`, `VERIFIED`, `SUSPENDED`)

* **Products**
  * Create, update, delete, and fetch products
  * Product attributes (size, color, etc.)
  * Stock management (`IN_STOCK`, `OUT_OF_STOCK`, `PRE_ORDER`)
  * Featured & new product tagging
  * Rating support (future)

* **Database**
  * MongoDB Atlas integration
  * Beanie ODM with indexes
  * Strong validation with Pydantic schemas

* **Developer Experience**
  * CORS enabled
  * Logging configured
  * Interactive API documentation with Swagger & ReDoc


## 🛠️ Tech Stack

- **Backend Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **Database**: [MongoDB Atlas](https://www.mongodb.com/atlas) (Cloud)
- **ODM**: [Beanie](https://beanie-odm.dev/)
- **Validation**: [Pydantic v2](https://docs.pydantic.dev/latest/)
- **Authentication**: JWT
- **Deployment**: [Render](https://render.com)

---

## 📂 Project Structure

```text
app/
│── auth/                 # Authentication routes & services
│── core/                 # Config, constants, logging
│── CART/                 # Cart business logic
│── database/             # Database initialization & repositories
│── models/               # Beanie models (User, Product, etc.)
│── schemas/              # Pydantic schemas (request & response)
│── products/             # Products Business logic
│── users/                # Users Business logic
│── utils/                # Reusable functions
│── main.py               # FastAPI entry point
requirements.txt          # App packages used

```

## ⚙️ Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/<your-org>/TrendLoom-Server.git
cd TrendLoom-Server
```

### 2. Create & activate virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

#### Create a .env file in the root directory

```bash
DATABASE_URL=your_mongodb_url
SECRET_KEY=your_secret_key
ALGORITHM=HS256
```

### 5. Run the server

```bash
fastapi dev app/main.py
```

Server will run at: <http://127.0.0.1:8000>

## 📖 API Documentation

* **Swagger UI**: /docs

* **ReDoc**: /redoc

## 🧪 Testing

```bash
pytest -v
```

## 🤝 Contributing

Contributions are welcome! To contribute:

* Fork the repo

* Create a new branch ```(git checkout -b feature/new-feature)```

* Commit changes ```(git commit -m 'Add new feature')```

* Push to branch ```(git push origin feature/new-feature)```

* Open a Pull Request
