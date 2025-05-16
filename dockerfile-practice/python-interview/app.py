from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()  # loads environment variables from .env file

app = Flask(__name__)

@app.route('/')
def index():
    return f"Hello, environment is {os.getenv('FLASK_ENV')}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

