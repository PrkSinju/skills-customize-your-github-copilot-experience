# 📘 Assignment: FastAPI REST API

## 🎯 Objective

Learn how to build a REST API using FastAPI and Pydantic models. Students will create endpoints for listing, retrieving, creating, and updating resources while validating request data.

## 📝 Tasks

### 🛠️ Build REST API Endpoints

#### Description
Create a FastAPI app with routes that support common API operations for an `Item` resource.

#### Requirements
Completed program should:

- Define a `FastAPI` application in `starter-code.py`.
- Create an `Item` Pydantic model with fields such as `id`, `name`, `description`, `price`, and `in_stock`.
- Implement the following endpoints:
  - `GET /items` to return a list of items
  - `GET /items/{item_id}` to return a single item by ID
  - `POST /items` to create a new item
  - `PUT /items/{item_id}` to update an existing item
- Return JSON responses and use proper HTTP status handling for missing items.

### 🛠️ Validate Input and Test the API

#### Description
Add input validation, query parameters, and test the API locally with Uvicorn.

#### Requirements
Completed program should:

- Use Pydantic models to validate request data.
- Accept query parameters or path parameters correctly.
- Start the app with `uvicorn starter-code:app --reload`.
- Demonstrate the API with at least one example request and response.

#### Example request

```bash
curl http://127.0.0.1:8000/items
```

#### Example response

```json
[
  {
    "id": 1,
    "name": "Widget",
    "description": "A useful widget",
    "price": 9.99,
    "in_stock": true
  }
]
```
