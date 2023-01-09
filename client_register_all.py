import requests

url = "http://127.0.0.1:5000/register"

users = [
    {'first_name': 'Tom', 'last_name': 'Smith', 'date_of_birth': '2000-01-01', 'email': 'tom@mail.com', 'password': 'easypassword'},
    {'first_name': 'Chris', 'last_name': 'Johnson', 'date_of_birth': '2000-01-01', 'email': 'chris@mail.com', 'password': 'easypassword'},
    {'first_name': 'Doe', 'last_name': 'Williams', 'date_of_birth': '2000-01-01', 'email': 'doe@mail.com', 'password': 'easypassword'},
    {'first_name': 'Katie', 'last_name': 'Brown', 'date_of_birth': '2000-01-01', 'email': 'katie@mail.com', 'password': 'easypassword'},
    {'first_name': 'Nero', 'last_name': 'Jones', 'date_of_birth': '2000-01-01', 'email': 'nero@mail.com', 'password': 'easypassword'},
    {'first_name': 'Patrick', 'last_name': 'Miller', 'date_of_birth': '2000-01-01', 'email': 'patrick@mail.com', 'password': 'easypassword'}
]

for user in users:
    response = requests.post(url, json=user)
    print(response.text)