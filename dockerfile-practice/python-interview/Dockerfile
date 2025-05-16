FROM python:3.11-slim

LABEL maintainer="kumzalelo23@gmail.com"

WORKDIR /app

# Copy only requirements first to leverage Docker cache
COPY requirements.txt .

# Install dependencies (make sure gunicorn is in requirements.txt)
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set environment variables
ENV FLASK_ENV=production

# Expose the port the app runs on
EXPOSE 8000

# Run the app with gunicorn binding to all interfaces on port 8000
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8000"]

