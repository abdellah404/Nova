# AgriWater AI Server Deployment

## Server

AgriWater AI is hosted on an Ubuntu Server.

The server uses:

* Docker
* Docker Compose
* PostgreSQL
* Git
* SSH through Tailscale

## Application Directory

The project is located at:

```text
/srv/agriwater
```

## Current Development Workflow

The project is developed locally on an Arch Linux laptop.

The workflow is:

1. Write and test code locally.
2. Create a Git commit.
3. Push the changes to GitHub.
4. Connect to the Ubuntu Server using SSH through Tailscale.
5. Pull the latest changes from GitHub.
6. Rebuild and restart the Docker services when needed.

## Database

PostgreSQL runs inside a Docker container on the Ubuntu Server.

The PostgreSQL database is not publicly exposed.

During local development, the FastAPI backend connects to PostgreSQL through an SSH tunnel.

The current development connection flow is:

```text
FastAPI on the development laptop
        ↓
localhost:5432
        ↓
SSH tunnel
        ↓
Ubuntu Server
        ↓
PostgreSQL Docker container
```

## Future Production Architecture

When FastAPI runs inside Docker on the Ubuntu Server, it will connect directly to PostgreSQL through the internal Docker network.

The future production connection will be:

```text
FastAPI container
        ↓
postgres:5432
        ↓
PostgreSQL container
```

The hostname `postgres` will be the name of the PostgreSQL service in Docker Compose.

No SSH tunnel will be required between the FastAPI and PostgreSQL containers.

## Secrets

The production `.env` file exists only on the Ubuntu Server.

The `.env` file must never be committed to GitHub.

A public `.env.example` file may be included in the repository to document the required environment variables without exposing real passwords or API keys.

## Deployment Status

Current status:

* [x] Ubuntu Server installed
* [x] Docker installed
* [x] Docker Compose installed
* [x] PostgreSQL running in Docker
* [x] SSH access configured through Tailscale
* [x] GitHub repository cloned to the server
* [x] Server environment file created
* [ ] FastAPI container deployed
* [ ] Angular container deployed
* [ ] Reverse proxy configured
* [ ] HTTPS configured
* [ ] Public domain configured
* [ ] Automated deployment configured

