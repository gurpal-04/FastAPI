# FastAPI Items API

A REST API built with FastAPI for creating and managing items. Items are stored in a local SQLite database (`items.db`) through SQLAlchemy.

## Features

- List, create, read, update, and delete items
- UUID-based item identifiers
- Partial updates for existing items
- Health and welcome endpoints
- Interactive API documentation at `/docs`

## Requirements

- Python 3.10 or later
- FastAPI
- Uvicorn
- SQLAlchemy
- pytest
- httpx

## Setup

From the project directory:

```bash
python -m venv venv
source venv/bin/activate
python -m pip install fastapi uvicorn sqlalchemy pytest httpx
```

On Windows, activate the virtual environment with:

```powershell
venv\Scripts\activate
```

## Run the API

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`. Interactive documentation is available at:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## API Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/` | Welcome message |
| `GET` | `/health` | Health status |
| `GET` | `/api/v1/items/` | List all items |
| `POST` | `/api/v1/items/` | Create an item |
| `GET` | `/api/v1/items/{item_id}` | Get an item by UUID |
| `PUT` | `/api/v1/items/{item_id}` | Partially update an item |
| `DELETE` | `/api/v1/items/{item_id}` | Delete an item |

### Item payload

Required fields for creation:

```json
{
  "title": "Learn pytest",
  "description": "Practice writing tests",
  "completed": false
}
```

Update payload fields are all optional:

```json
{
  "title": "Learn pytest",
  "completed": true
}
```

### Example requests

Check the health endpoint:

```bash
curl http://127.0.0.1:8000/health
```

Create an item:

```bash
curl -X POST http://127.0.0.1:8000/api/v1/items/ \
  -H "Content-Type: application/json" \
  -d '{"title":"Learn pytest","description":"Practice writing tests","completed":false}'
```

List items:

```bash
curl http://127.0.0.1:8000/api/v1/items/
```

## Running Tests

```bash
pytest
```

Tests run against the API through FastAPI's `TestClient`. Be aware that API tests that create items use the configured SQLite database unless the test suite redirects or replaces the database session.

## Project Structure

```text
app/
  main.py                 # FastAPI application and startup configuration
  api/v1/items.py         # Item CRUD routes
  db/database.py          # SQLite engine and database session
  models/items.py         # SQLAlchemy Item model
  schemas/item_schema.py  # Pydantic request and response schemas
tests/
  test_items.py           # API tests
items.db                  # SQLite database (created automatically)
```
