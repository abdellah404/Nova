# Remote PostgreSQL Development

## Architecture

FastAPI runs on the development laptop.

PostgreSQL runs in Docker on the Ubuntu Server.

The development laptop connects to PostgreSQL through an SSH tunnel.

## Start PostgreSQL on the server

```bash
cd ~/agriwater/infrastructure
docker compose up -d


Create the SSH tunnel
ssh -N -L 5432:localhost:5432 USER@SERVER_IP



Run FastAPI locally
uvicorn app.main:app --reload