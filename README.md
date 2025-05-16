README
---

# Docker & Flask Practice

This repository contains practice exercises and examples for containerizing Python Flask applications using Docker, focusing on real-world production scenarios.

## What You’ll Learn

* Writing Dockerfiles for Python Flask apps with:

  * Base images (`python:3.11-slim`)
  * Dependency management with `requirements.txt`
  * Best practices for layering and caching
  * Using production-grade servers like `gunicorn`
  * Setting environment variables inside containers

* Managing `.dockerignore` files to optimize builds and security

* Handling environment variables and secrets securely (e.g., `.env` files)

* Creating Docker Compose configurations for multi-container apps:

  * Flask web app + PostgreSQL database
  * Service communication via Docker networks
  * Volume management for data persistence

* Common pitfalls and error fixes when pushing code to GitHub from a Linux server

---

## How to Use

* Build and run Flask Docker images with `docker build` and `docker run`
* Compose multi-service stacks with `docker-compose up`
* Modify Dockerfiles to add your own app code and dependencies
* Practice troubleshooting Docker, Git, and deployment workflows

---

ReadMe will expand as I continue learning :)

---


