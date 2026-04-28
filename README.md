# College Management API

A FastAPI-based backend for managing college data, including students, courses, and their relationships. The project uses SQLAlchemy with a SQLite database and includes JWT-based authentication for protected endpoints. A Dockerfile is provided for containerized deployment.

## Features

- **Student management** (create, list, update, delete)
- **Course management** (create, list, update, delete)
- **Many-to-many relationship** between students and courses
- **JWT authentication** with admin credentials
- **SQLite database** stored in `data/college.db`
- **Docker support** for easy deployment

## Tech Stack

- **FastAPI**
- **SQLAlchemy**
- **SQLite**
- **Pydantic**
- **JWT (python-jose)**
- **Uvicorn**

## Project Structure

```
.
├── app/
│   ├── main.py        # API routes and app entrypoint
│   ├── auth.py        # JWT auth utilities
│   ├── crud.py        # Database operations
│   ├── models.py      # SQLAlchemy models
│   ├── schemas.py     # Pydantic schemas
│   └── database.py    # DB engine and session
├── data/
│   └── college.db     # SQLite database
├── Dockerfile
├── requirements.txt
└── README.md
```

## Setup (Local)

### 1. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set environment variables

Create a `.env` file in the project root:

```env
ADMIN_USERNAME=admin
ADMIN_PASSWORD=admin123
SECRET_KEY=your-secret-key
```

### 4. Run the app

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## Authentication

The API uses OAuth2 with password flow. Tokens expire after 30 minutes.

**Login endpoint:**

```
POST /login
```

Submit `username` and `password` as form data to receive an access token. Use the returned token as a `Bearer` token in the `Authorization` header when calling all other endpoints.

## API Endpoints

### Auth

| Method | Path     | Description          | Auth required |
|--------|----------|----------------------|---------------|
| POST   | `/login` | Obtain a JWT token   | No            |

### Students

| Method | Path                    | Description           | Auth required |
|--------|-------------------------|-----------------------|---------------|
| POST   | `/students`             | Create a student      | Yes           |
| GET    | `/students`             | List all students     | Yes           |
| PUT    | `/students/{student_id}`| Update a student      | Yes           |
| DELETE | `/students/{student_id}`| Delete a student      | Yes           |

### Courses

| Method | Path                   | Description          | Auth required |
|--------|------------------------|----------------------|---------------|
| POST   | `/courses`             | Create a course      | Yes           |
| GET    | `/courses`             | List all courses     | Yes           |
| PUT    | `/courses/{course_id}` | Update a course      | Yes           |
| DELETE | `/courses/{course_id}` | Delete a course      | Yes           |

Interactive API documentation is available at `http://127.0.0.1:8000/docs` once the server is running.

## Docker

Build and run with Docker:

```bash
docker build -t college-management .
docker run -p 8000:8000 \
  -e ADMIN_USERNAME=admin \
  -e ADMIN_PASSWORD=admin123 \
  -e SECRET_KEY=your-secret-key \
  college-management
```

The API will be available at `http://localhost:8000`.

## License

No license specified.