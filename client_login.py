import requests

url = "http://127.0.0.1:5000/login"
data = {'email': 'johndoe@example.com', 'password': 'password'}

response = requests.post(url, json=data)

print(response.text)
