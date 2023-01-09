import requests

url = "http://127.0.0.1:5000/register"
data = {'first_name': 'John', 'last_name': 'Doe', 'date_of_birth': '2000-01-01', 'email': 'johndoe@example.com', 'password': 'password'}

response = requests.post(url, json=data)

print(response.text)
