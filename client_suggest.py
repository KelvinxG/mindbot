from werkzeug.security import generate_password_hash
import json

# def takeinputs(f,l,email,password):
#     user_info={"firstname":f,"lastname":l,
#     "email":email,"password":password}
#     #write it down onto .txt

#     with open("test.txt","a") as f:
#         f.write(json.dumps(user_info))
#         f.write("\n")

#     return print("user added")

    
# takeinputs(f="John",l="Coner",email="myemail@gmail.com",password="test123")
# takeinputs(f="John",l="Wick",email="myemail2@gmail.com",password="test123")


import requests

url = "http://127.0.0.1:5000/suggest-booking"
params = {'seat': 2}
headers = {'Authorization': 'Bearer valid_token'}

response = requests.get(url, params=params, headers=headers)

print(response.json())
