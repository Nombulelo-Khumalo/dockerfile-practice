Create a Dockerfile for a Flask web app that:

Uses a requirements.txt file for dependencies

Serves HTML templates from a templates/ folder

Uses a static/ folder for CSS

Expects an environment variable called APP_ENV

Defaults to running on port 8000 instead of 5000


Goals for your Dockerfile:
Use python:3.11-slim

Install dependencies from requirements.txt

Set environment variable APP_ENV=production inside the container

Expose port 8000

Copy all files (including templates/ and static/)

Start the app


