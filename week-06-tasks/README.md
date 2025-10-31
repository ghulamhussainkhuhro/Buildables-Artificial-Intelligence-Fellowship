### **Week 06 – API Development**

This week focuses on building, testing, and securing RESTful APIs using **Flask** and **FastAPI**.
The work is divided into three tasks that progressively build your understanding — from a simple in-memory API to a secure, persistent API with authentication.

---

## **Folder Structure**

```
Week_06_API_Development/
│
├── flask_app/                # Task 1: Basic Flask API
│   ├── app.py
│   └── __init__.py
│
├── fastapi_app/              # Task 2: FastAPI rewrite with validation
│   ├── main.py
│   ├── todos.json
│   └── __init__.py
│
├── task3_auth_api/           # Task 3: Authentication and DELETE endpoint
│   ├── main.py
│   └── todos.json
│
├── utils/
│   └── sample_requests.md
│
├── snippets/
│   └── example_commands.md
│
├── notes.ipynb
├── requirements.txt
└── README.md
```

---

## **Task 1 – Basic RESTful API in Flask**

**Objective:**
Create a simple Flask API that allows users to manage a list of to-do items stored in memory.

**Endpoints:**

| Method | Endpoint | Description             |
| ------ | -------- | ----------------------- |
| GET    | `/todos` | Returns all to-do items |
| POST   | `/todos` | Adds a new to-do item   |

**Key Concepts:**

* Flask app setup and routing
* GET and POST HTTP methods
* Returning JSON responses with status codes
* Using an in-memory list as a temporary database

**Run the API:**

```bash
cd flask_app
python app.py
```

**Test the Endpoints:**

```bash
# Retrieve all todos
curl http://127.0.0.1:5000/todos

# Add a new todo (PowerShell format)
curl -Method POST http://127.0.0.1:5000/todos `
     -Headers @{ "Content-Type" = "application/json" } `
     -Body '{"task": "Complete API assignment"}'
```

---

## **Task 2 – Rewrite in FastAPI with Type Hints**

**Objective:**
Rebuild the same to-do API using **FastAPI**, adding type hints and data validation with Pydantic.
Data is now stored persistently in a `todos.json` file instead of in memory.

**Endpoints:**

| Method | Endpoint | Description             |
| ------ | -------- | ----------------------- |
| GET    | `/todos` | Returns all to-do items |
| POST   | `/todos` | Adds a new to-do item   |

**Key Concepts:**

* Type hints for request and response models
* Pydantic-based data validation
* Persistent JSON storage
* Auto-generated documentation via `/docs`

**Run the API:**

```bash
uvicorn fastapi_app.main:app --reload
```

**Access the API documentation:**

```
http://127.0.0.1:8000/docs
```

---

## **Task 3 – Extend with Authentication and DELETE Endpoint**

**Objective:**
Extend the FastAPI application to include simple API key authentication and a DELETE endpoint.

**Authentication Setup:**

* The `.env` file is located in the project root.
* It contains an API key in the format:

```
API_KEY=secret123
```

**Endpoints:**

| Method | Endpoint      | Authentication | Description         |
| ------ | ------------- | -------------- | ------------------- |
| GET    | `/todos`      | Not required   | Retrieve all todos  |
| POST   | `/todos`      | Required       | Add a new todo      |
| DELETE | `/todos/{id}` | Required       | Delete a todo by ID |

**Key Concepts:**

* Environment variable loading using `python-dotenv`
* API key validation through request headers
* Error handling for unauthorized access and missing resources
* DELETE operation to remove items by ID

**Run the API:**

```bash
uvicorn task3_auth_api.main:app --reload
```

**Test via Swagger UI:**
Open:

```
http://127.0.0.1:8000/docs
```

**Add the header in Swagger UI or Postman:**

```
X-API-Key: secret123
```

**Example request body for POST:**

```json
{
  "task": "Learn FastAPI Authentication"
}
```

**Example DELETE request:**

```
DELETE /todos/1
Header: X-API-Key: secret123
```

---

## **Snippets and Utilities**

The `snippets/` and `utils/` directories include:

* Example PowerShell and curl commands for testing endpoints.
* Sample JSON payloads.
* `.env` template and environment variable usage examples.
* Notes on common HTTP status codes.

---

## **Key Learnings**

| Concept                | Description                                  |
| ---------------------- | -------------------------------------------- |
| REST API Basics        | Designing APIs with standard HTTP methods    |
| Flask                  | Setting up and handling routes and responses |
| FastAPI                | Leveraging type hints and Pydantic models    |
| Environment Variables  | Managing secrets securely via `.env`         |
| Authentication         | Validating requests using custom headers     |
| File-based Persistence | Storing and retrieving data from JSON files  |
| Swagger Documentation  | Interactive API testing through `/docs`      |

---

## **Dependencies**

Install dependencies before running any of the tasks:

```bash
pip install -r requirements.txt
```

Typical packages:

```
flask
fastapi
uvicorn
python-dotenv
pydantic
```

---

## **Next Steps**

* Implement a `PUT /todos/{id}` endpoint to update tasks.
* Replace JSON file storage with a database (e.g., SQLite or PostgreSQL).
* Deploy the FastAPI app using platforms such as Render, Railway, or Hugging Face Spaces.

---

**End of Week 06 – API Development**



