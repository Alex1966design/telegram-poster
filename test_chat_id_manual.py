import requests

# ВСТАВЬ СЮДА СВОЙ РЕАЛЬНЫЙ ТОКЕН — в кавычках!
TOKEN = "7598269211:AAH5zTrpyfQ5R1fGUS6M8rSi_vD-GgE_DOI"

url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"

response = requests.get(url)

print("Status code:", response.status_code)
print("Ответ от Telegram:")
print(response.text)
