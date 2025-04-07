import os
import requests
from dotenv import load_dotenv

load_dotenv()
from pathlib import Path

print("Текущая рабочая директория:", Path.cwd())
print(".env найден?", Path(".env").exists())
print("TELEGRAM_BOT_TOKEN:", os.getenv("TELEGRAM_BOT_TOKEN"))
print("TELEGRAM_CHAT_ID:", os.getenv("TELEGRAM_CHAT_ID"))

TOKEN = os.getenv("7598269211:AAH5zTrpyfQ5R1fGUS6M8rSi_vD-GgE_DOI")

# 💡 добавь это:
print("Загруженный токен:7598269211:AAH5zTrpyfQ5R1fGUS6M8rSi_vD-GgE_DOI", )

url = f"https://api.telegram.org/bot{7598269211:AAH5zTrpyfQ5R1fGUS6M8rSi_vD-GgE_DOI}

response = requests.get(url)
print(response.status_code)
print(response.text)
