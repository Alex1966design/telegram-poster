import os
import requests
from flask import Flask, request
from pathlib import Path

# Загружаем .env только локально
if Path(".env").exists():
    from dotenv import load_dotenv
    load_dotenv()

# Отладочный вывод
print("📂 Текущая рабочая директория:", Path.cwd())
print("📄 Файл .env найден?", Path(".env").exists())
print("🔐 TELEGRAM_BOT_TOKEN:", os.getenv("TELEGRAM_BOT_TOKEN"))
print("💬 TELEGRAM_CHAT_ID:", os.getenv("TELEGRAM_CHAT_ID"))

# Чтение переменных окружения
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# Проверка наличия переменных
if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
    raise ValueError("❌ Не найден TELEGRAM_BOT_TOKEN или TELEGRAM_CHAT_ID. Проверь переменные окружения.")

# Flask-приложение
app = Flask(__name__)

@app.route("/", methods=["POST"])
def post_to_telegram():
    data = request.json
    message = data.get("message", "⚠️ Сообщение не получено")

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }

    response = requests.post(url, json=payload)
    return {
        "status": "ok",
        "telegram_response": response.json()
    }

if __name__ == "__main__":
    # ⚠️ Обязательно указываем host и port для Koyeb
    app.run(debug=True, host="0.0.0.0", port=8000)
