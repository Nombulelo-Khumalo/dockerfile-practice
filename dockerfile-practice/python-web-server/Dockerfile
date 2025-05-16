FROM python:3.11-slim

LABEL maintainer="kumzalelo23@gmail.com"

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ..

RUN pip install flask

EXPOSE 5000

CMD ["python", "app.py"]
