# Secure NFC Access Control System

A Flask-based NFC access control backend. It stores users, NFC cards, and access decisions in SQLite and exposes a small JSON API for registration and authorization.

## Features

- Create users with a role.
- Register an NFC card to an existing user.
- Authorize NFC scans for active cards.
- Record granted and denied access attempts.
- Simulate NFC reader and virtual card behavior through the backend modules.

## Project Structure

```text
backend/
  run.py                 Flask application entry point
  app/
    api/                 User, NFC card, and scan endpoints
    database/            SQLAlchemy database setup
    models/              User, card, and access log models
    simulator/           NFC reader and virtual card helpers
docs/                    Documentation workspace
frontend/                Frontend workspace
tests/                   Test workspace
```

## Requirements

- Python 3.9 or newer
- Flask
- Flask-SQLAlchemy

## Run Locally

From the repository root:

```powershell
cd backend
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install Flask Flask-SQLAlchemy
python run.py
```

The API starts in debug mode at `http://127.0.0.1:5000`.

The SQLite database is created locally as `backend/instance/access_control.db` and is intentionally ignored by Git.

## API Endpoints

### Health check

```http
GET /
```

### Create a user

```http
POST /api/users
Content-Type: application/json

{
  "name": "Alex Smith",
  "email": "alex@example.com",
  "role": "employee"
}
```

### Register an NFC card

```http
POST /api/nfc-cards
Content-Type: application/json

{
  "card_uid": "04AABBCCDD",
  "card_name": "Front Door Card",
  "user_id": 1
}
```

### Scan an NFC card

```http
POST /api/nfc-scan
Content-Type: application/json

{
  "card_uid": "04AABBCCDD"
}
```

An active registered card returns `GRANTED`. Unknown or inactive cards return `DENIED` and create an access log entry.

## Notes

- The local Python virtual environment, SQLite database, logs, and generated files are excluded through `.gitignore`.
- Do not commit production credentials or private NFC card data.
- Tests and frontend components can be added in the existing `tests/` and `frontend/` directories.