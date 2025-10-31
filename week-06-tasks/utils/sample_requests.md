# **Sample Requests and Responses**

This file provides example request and response payloads for all **Week 06 API Development Tasks**.

---

## 🧩 **Task 1 – Flask To-Do API**

### ▶️ **GET /todos**

**Request:**

```http
GET /todos
```

**Response:**

```json
{
  "status": "success",
  "data": [
    { "id": 1, "task": "Buy groceries" },
    { "id": 2, "task": "Study Flask APIs" }
  ]
}
```

---

### ▶️ **POST /todos**

**Request Body:**

```json
{
  "task": "Complete Flask assignment"
}
```

**Response:**

```json
{
  "status": "success",
  "message": "Todo added successfully!",
  "data": { "id": 3, "task": "Complete Flask assignment" }
}
```

---

## ⚡ **Task 2 – FastAPI To-Do API**

### ▶️ **GET /todos**

**Request:**

```http
GET /todos
```

**Response:**

```json
[
  { "id": 1, "task": "Learn FastAPI" },
  { "id": 2, "task": "Test with Swagger UI" }
]
```

---

### ▶️ **POST /todos**

**Request Body:**

```json
{
  "task": "Build FastAPI version of To-Do app"
}
```

**Response:**

```json
{
  "id": 3,
  "task": "Build FastAPI version of To-Do app"
}
```

**💡 Test via Swagger UI:**
Visit [`http://127.0.0.1:8000/docs`](http://127.0.0.1:8000/docs) in your browser.

---

## 🔐 **Task 3 – Authenticated FastAPI API**

### ▶️ **Headers (Required for Authenticated Routes)**

```http
X-API-Key: secret123
```

---

### ▶️ **GET /todos**

**Request:**

```http
GET /todos
```

**Response:**

```json
{
  "status": "success",
  "data": [
    { "id": 1, "task": "Secure FastAPI endpoints" },
    { "id": 2, "task": "Implement DELETE method" }
  ]
}
```

---

### ▶️ **POST /todos**

**Request Headers:**

```
X-API-Key: secret123
```

**Request Body:**

```json
{
  "task": "Test authenticated POST request"
}
```

**Response:**

```json
{
  "status": "success",
  "message": "Todo added successfully!",
  "data": { "id": 3, "task": "Test authenticated POST request" }
}
```

---

### ▶️ **DELETE /todos/{id}**

**Request Example:**

```
DELETE /todos/3
X-API-Key: secret123
```

**Response:**

```json
{
  "status": "success",
  "message": "Todo deleted successfully!"
}
```

**If invalid API key:**

```json
{
  "status": "error",
  "message": "Unauthorized: Invalid API key"
}
```

**If ID not found:**

```json
{
  "status": "error",
  "message": "Todo not found"
}
```

---

## 🧠 **Quick Testing Notes**

| Task         | Auth Needed | Methods           | Swagger Docs    |
| ------------ | ----------- | ----------------- | --------------- |
| Flask        | ❌ No        | GET, POST         | ❌ Not available |
| FastAPI      | ❌ No        | GET, POST         | ✅ `/docs`       |
| Auth FastAPI | ✅ Yes       | GET, POST, DELETE | ✅ `/docs`       |

---

✅ **You can copy these examples into Postman or Swagger UI directly for quick testing.**
Each example uses minimal JSON and clear key names to make debugging simple.

