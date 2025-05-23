from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    env = os.getenv("APP_ENV", "development")
    return render_template("index.html", env=env)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

