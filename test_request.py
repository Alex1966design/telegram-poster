import requests

url = "http://127.0.0.1:5000/"
payload = {
    "message": "Привет из Python-скрипта! 👋"
}

response = requests.post(url, json=payload)

print("Status code:", response.status_code)
print("Response:", response.json())
