# devops-app-pipeline

A small Python web app taken step by step through a full DevOps workflow: Docker, CI/CD, Kubernetes and Terraform. Built to learn how the pieces fit together.

## Phase 1: Docker Compose (done)
A Flask web app counts page visits and stores the count in Redis. The app and the database run as two separate containers on one private network.

- `app.py`: the web app, with a `/health` endpoint
- `requirements.txt`: Python dependencies
- `Dockerfile`: builds the app image from a slim Python base
- `docker-compose.yml`: runs the app and Redis together; the app finds Redis by its service name

### Run it
You need Docker Desktop running. From this folder:

    docker compose up --build

Then open `localhost:5000`. Stop and remove everything with:

    docker compose down

### Result
![App running in Docker](app-running.png)

## Roadmap
- Phase 2: GitHub Actions builds the image and pushes it to Docker Hub
- Phase 3: deploy to Kubernetes on a local cluster
- Phase 4: create the AWS server with Terraform

## What I learned
Containers find each other by service name, and restarting the app does not lose data stored in a separate database container.

## Tools
Python, Flask, Redis, Docker, Docker Compose
