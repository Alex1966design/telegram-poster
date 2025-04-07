import requests

url = "http://127.0.0.1:5000/"
payload = {
    "message": "✅ Привет из локального Python-бота! Всё работает!"
}

response = requests.post(url, json=payload)

print("Status code:", response.status_code)
print("Response:", response.json())
