Scenario 4 — Real-World / Interview-Level
“You're given a Python Flask application with multiple dependencies, a .env file for secrets, and it connects to a PostgreSQL database.
Dockerize this app for production, using best practices.”

💼 Requirements
Use python:3.11-slim as your base image

Install dependencies from requirements.txt

Copy the entire app (including templates/, static/, .env, etc.)

Use gunicorn as the WSGI server instead of flask run

Read environment variables from a .env file (use python-dotenv)

Expose port 8000

Set environment variable FLASK_ENV=production inside the container

Make sure the container starts the app using gunicorn

Organize the Dockerfile with proper layering for caching

Use a .dockerignore to avoid copying unnecessary files (e.g. __pycache__, .venv/, .git/)


 Goal
Write the Dockerfile and .dockerignore for this project.
Don’t worry about docker-compose yet (we'll do that next if you want). Focus on the Dockerfile as if you're deploying this on a container orchestration platform.
