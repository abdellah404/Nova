# AgriWater AI

AgriWater AI is a smart irrigation platform designed to help farmers monitor field conditions and make better irrigation decisions.

The project combines:

* Angular
* FastAPI
* PostgreSQL
* Docker
* Simulated IoT sensor data
* AI-based irrigation recommendations
* Cloud deployment

## Current Status

🚧 The project is under active development.

Current progress:

* Angular frontend initialized
* FastAPI backend initialized
* PostgreSQL configured with Docker
* Field model implemented
* Field creation endpoint implemented
* Field retrieval endpoint implemented

## Architecture

```text
Angular
   ↓
FastAPI
   ↓
SQLAlchemy
   ↓
PostgreSQL
```

## Local Setup

### Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Create the environment file:

```bash
cp .env.example .env
```

Start the API:

```bash
uvicorn app.main:app --reload
```

The API documentation is available at:

```text
http://localhost:8000/docs
```

### Database

Start PostgreSQL:

```bash
docker compose up -d
```

Stop PostgreSQL:

```bash
docker compose down
`
