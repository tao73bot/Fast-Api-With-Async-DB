# FAST API CRUD with MongoDB

## I follow this folder structure

```paintext
project/
│
├── .venv/                      # Virtual environment
│
├── apps/                       # Application-specific modules
│   ├── user/                   # User-related module
│   │   ├── models.py           # MongoDB models (e.g., User model)
│   │   ├── service.py          # Data access logic (CRUD operations)
│   │   ├── routes.py           # Routes for user-related endpoints
│   │   ├── schemas.py          # Pydantic schemas for User validation
│   │   └── utils/              # Utils directory (business logic)
│   │       └── auth_service.py # Authentication logic
│   │
│   └── todo/                   # Todo-related module
│       ├── models.py           # MongoDB models (e.g., Todo model)
│       ├── service.py          # Data access logic (CRUD operations)
│       ├── routes.py           # Routes for todo-related endpoints
│       └── schemas.py          # Pydantic schemas for Todo validation
│
├── config.py                   # Configuration settings for the project
├── Dockerfile
├── main.py                     # FastAPI application entry point
├── requirements.txt            # List of project dependencies
├── .env                        # Environment variables (should not be in version control)
├── .gitignore
├── celery_worker.py            # Git ignore file to exclude unwanted files/folders
└── README.md                   # Project documentation

```

## Table of Contents

1. [Installation](#installation)  
2. [Running the Project](#running-the-project)  
3. [API Endpoints](#api-endpoints)  
   - [User Endpoints](#user-endpoints)  
   - [Task Endpoints](#task-endpoints)  
4. [Authentication](#authentication)  
5. [Environment Variables](#environment-variables)  
6. [Database](#database)
7. [Database Migration](#database-migration)  
8. [Celery](#celery)
9. [Docker](#docker)
10. [Testing](#testing)  
11. [Contributing](#contributing)  
12. [License](#license)

## Installation

### Prerequisites

Ensure the following are installed on your system:

- Python 3.6 or higher
- Postgresql

### Steps

1. **Clone the repository**  
   Clone the project repository to your local machine:
   ```bash
   git clone https://github.com/your-repo-name.git
   cd your-repo-name
   ```

2. **Create and Activate virtual enviroment**  
    To do that run the following command
   ```bash
   # Create virtual enviroment
   python -m venv .venv
   # Acticate virtual enviroment
   source .venv/bin/activate # on mac and linux
   venv\Scripts\activate # on windows
   ```

3. **Install dependencies**  
    Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Project

Once the installation is complete, follow these steps to run the FastAPI application:

1. **Start the server**  
   Use `uvicorn` to start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

- The `--reload` flag enables automatic code reload during development.


2. **Access the application**  
    By default, access point is:
    - **Base URL** `127.0.0.1:8000`

3. **Explore Api documentations**  
    Fast api provides interactive API documentation at these endpoints:
    - **Swagger UI** : http://127.0.0.1:8000/docs
    - **Redoc UI** : http://127.0.0.1:8000/redoc

### Run on different port
Use the `--port` flag to run the server on a custom port:
```bash
uvicorn main:app --reload --port 8080
```

## API Endpoints
### User Endpoints

`POST /users/signup`
- **Description**: Create a new user.
- **Parameters**: None
- **Request body**:
```json
{
    "username": "string",
    "email": "user@example.com",
    "password": "string"
}
```
- **Response**:
```json
{
    "id": "string",
    "username": "string",
    "email": "user@example.com" 
}
```

`POST /users/login`
- **Description**: Login as user.
- **Parameters**: None
- **Request body**:
```json
{
    "username": "string",
    "email": "user@example.com",
    "password": "string"
}
```
- **Response**:
```json
{
    "message": "Login successful",
    "access_token": "access_token",
    "refresh_token": "refresh_token",
    "user": {
        "username": "string",
        "email": "user@example.com",
        "id": "string"
    }
}
```

### Task Endpoints




## Authentication

- **Mechanism**: Bearer Token (JWT)
- **Endpoints**:
    - `POST /users/login` to get token
    - Use the token in the `Authorization` header:
    ```bash
    Authorization: Bearer <your_token>
    ```

## Environment Variables
Create a `.env` file in the root directory with the following keys:
```.env
DB_URL="postgresql+asyncpg://username:password@localhost/db_name"
DB_NAME="db_name"

# JWT Configuration
JWT_SECRET="mysecrect"
JWT_ALGORITHM="Algorithm"
JWT_EXPIRY=30  # Can be "30m", "1h", "15m", etc.

```

- **Config the settings using `.env` file**

## Database
- **Database Type**: Postgresql
- **ORM**: `sqlalchemy`
- **Setup**: Use database `URI` from `.env` file

## Database Migration

**Mirgration using Alembic**
- Initialize Alembic
```bash
alembic init -t async alembic
```
- Add Changes in the model
- Modify **env.py** file
```bash
from config import Base # import Base
target_metadata = Base.metadata # Replace with your metadata
```
- Create Migration file
```bash
alembic revision --autogenerate -m "message"
```
- Go to the **versions/<migration_id>_file_name.py** file and check the upgrade and downgrade functions
- Apply the migration
```bash
alembic upgrade head
```
- See migration history
```bash
alembic history
```
- Downgrade to the Previous Revision
```bash
alembic downgrade -1
```
- Downgrade to the Specific Revision
```bash
alembic downgrade <revision_id>
```

## Celery
- I use celery with redis.
- Connection of broker and backend
```bash
broker='redis://localhost:6379/0',
backend='redis://localhost:6379/0'
```
- Run Celery Worker in a seperate terminal and make sure you are inside apps
```bash
celery -A celery_worker.celery_app worker --loglevel=info
```
- Celery Flower Monitoring Tool(Run in a seperate terminal)
```bash
celery -A celery_worker.celery_app flower --port=5555
```

## Docker

- **Create an Image**
```bash
sudo docker build -t < image-name > .
```

- **List of Images**
```bash
sudo docker images
```

- **Run the Docker Container**
```bash
sudo docker run -d -p 8000:8000 < image-name >
```

- **Run docker container using host network**
```bash
sudo docker run --network host -d -p 8000:8000 < image-name >
```

- **List of Containers**
```bash
sudo docker ps
```

- **Stop the Docker container**
```bash
sudo docker stop <container_id>
```

- **Save an image**
```bash
sudo docker save -o fastapi-postgres.tar fastapi-postgres
```

- **ID of exited containers**
```bash
sudo docker ps -a
```

- **Container Logs**
```bash
sudo docker logs <container_id>
```

- **Remove a Container**
```bash
sudo docker rm <container_id>
```

- **Remove an Image**
```bash
sudo docker rmi <imgae_id>
```