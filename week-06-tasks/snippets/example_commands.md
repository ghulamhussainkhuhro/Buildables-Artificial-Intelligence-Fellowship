# **Example API Commands**

This document provides ready-to-use commands for testing all three tasks in **Week 06 – API Development**.
Each section corresponds to one task, showing `GET`, `POST`, and `DELETE` (if available) examples.

---

## **Task 1 – Flask To-Do API**

### Base URL

```
http://127.0.0.1:5000
```

### 1. Get All Todos

```bash
curl http://127.0.0.1:5000/todos
```

### 2. Add a New Todo (PowerShell)

```bash
curl -Method POST http://127.0.0.1:5000/todos `
     -Headers @{ "Content-Type" = "application/json" } `
     -Body '{"task": "Complete Flask assignment"}'
```

### 3. Expected Response

```json
{
  "status": "success",
  "message": "Todo added successfully!",
  "data": {
    "id": 1,
    "task": "Complete Flask assignment"
  }
}
```

---

## **Task 2 – FastAPI To-Do API**

### Base URL

```
http://127.0.0.1:8000
```

### 1. Get All Todos

```bash
curl http://127.0.0.1:8000/todos
```

### 2. Add a New Todo (PowerShell)

```bash
curl -Method POST http://127.0.0.1:8000/todos `
     -Headers @{ "Content-Type" = "application/json" } `
     -Body '{"task": "Learn FastAPI"}'
```

### 3. Test via Swagger UI

Open:

```
http://127.0.0.1:8000/docs
```

You can run both `GET` and `POST` directly in the browser without additional tools.

---

## **Task 3 – FastAPI with Authentication and DELETE**

### Base URL

```
http://127.0.0.1:8000
```

### API Key Header

All write/delete requests require a valid API key defined in `.env`:

```
X-API-Key: secret123
```

### 1. Get All Todos (No Authentication Required)

```bash
curl http://127.0.0.1:8000/todos
```

### 2. Add a New Todo (Authenticated)

```bash
curl -Method POST http://127.0.0.1:8000/todos `
     -Headers @{ 
        "Content-Type" = "application/json"; 
        "X-API-Key" = "secret123" 
     } `
     -Body '{"task": "Write authenticated FastAPI code"}'
```

### 3. Delete a Todo by ID (Authenticated)

```bash
curl -Method DELETE http://127.0.0.1:8000/todos/1 `
     -Headers @{ "X-API-Key" = "secret123" }
```

### 4. Expected DELETE Response

```json
{
  "status": "success",
  "message": "Todo deleted successfully!"
}
```

---

## **Quick Reference**

| Task | Framework | Auth Required     | Endpoints                                         |
| ---- | --------- | ----------------- | ------------------------------------------------- |
| 1    | Flask     | ❌ No              | `GET /todos`, `POST /todos`                       |
| 2    | FastAPI   | ❌ No              | `GET /todos`, `POST /todos`                       |
| 3    | FastAPI   | ✅ Yes (X-API-Key) | `GET /todos`, `POST /todos`, `DELETE /todos/{id}` |

---

## **Tips**

* Always start the corresponding app before running the curl commands.
* PowerShell uses backticks (```) for multiline commands — remove them if running on Linux/macOS.
* Use `uvicorn` for FastAPI and `python` for Flask.
* Use `/docs` for FastAPI tasks to interact visually with the API.

---

**End of File – example_commands.md**