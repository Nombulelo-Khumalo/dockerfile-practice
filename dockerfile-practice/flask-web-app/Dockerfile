FROM python:3.11-slim

LABEL maintainer="kumzalelo23@gmail.com"

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

ENV APP_ENV=production

CMD ["python", "app.py",]

