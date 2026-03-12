from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def index():
    # Берем токен из переменной окружения
    token = os.getenv("TOKEN_HASH8", "missing_token")
    return f"Hello from Docker! TOKEN_HASH8={token}\n"

if __name__ == "__main__":
    # threaded=False отключает создание новых потоков для запросов
    app.run(host="0.0.0.0", port=8080, threaded=False)