# FastAPI Items API

A small REST API built with FastAPI for creating and managing items. Items are stored locally in `app/db/tasks.json`.

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
- pytest
- httpx

## Setup

From the project directory:

```bash
python -m venv venv
source venv/bin/activate
python -m pip install fastapi uvicorn pytest httpx
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

Tests use a temporary JSON database file, so they do not modify `app/db/tasks.json`.

## Project Structure

```text
app/
  main.py                 # FastAPI application and root routes
  api/v1/items.py         # Item CRUD routes
  db/db.py                # JSON file database helpers
  db/tasks.json           # Local item data
  models/items.py         # Pydantic request and response models
tests/
  test_items.py           # API tests
```
