from flask import Flask ,render_template,request,flash,jsonify
from werkzeug.security import generate_password_hash,check_password_hash
import datetime
import json
import secrets
import jwt


#initialize the app
app=Flask(__name__)


#basic app config
app.config['SECRET_KEY']=secrets.token_hex(16)


#booked
bookings = {
    'A': {'3': 'tom@mail.com', '4': 'tom@mail.com', '6': 'mary@mail.com', '7': 'mary@mail.com'},
    'B': {'1': 'chris@mail.com', '2': 'chris@mail.com', '3': 'chris@mail.com', '5': 'doe@mail.com', '6': 'doe@mail.com', '7': 'doe@mail.com', '8': 'doe@mail.com'},
    'C': {'7': 'doe@mail.com', '8': 'doe@mail.com'},
    'D': {'4': 'katie@mail.com'},
    'E': {'2': 'nero@mail.com', '3': 'nero@mail.com', '7': 'patrick@mail.com', '8': 'patrick@mail.com'}
}



#index page
@app.route('/')
def index():
    return "Welcome to Booking System"

#to register and dump information onto .txt file
@app.route('/register', methods=["POST"])
def register():
    data = request.get_json()
    first_name = data['first_name']
    last_name = data['last_name']
    date_of_birth = data['date_of_birth']
    email = data['email']
    password = data['password']
    user = {'first_name': first_name, 'last_name': last_name, 'date_of_birth': date_of_birth, 'email': email, 'password': password}
    with open('users.txt', 'a') as f:
        f.write(json.dumps(user) + '\n')
    return 'User registered successfully'

@app.route('/login', methods=["POST","GET"])
def login():
    data = request.get_json()
    email = data['email']
    password = data['password']
    with open('users.txt') as f:
        for line in f:
            user = json.loads(line)
            if user['email'] == email and user['password'] == password:
                payload = {
                    'email': email,
                    'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)
                }
                token = jwt.encode(payload, 'secret', algorithm='HS256')
                return token
    return 'Invalid email or password', 401


#create a booking system
@app.route('/suggest-booking', methods=['GET'])
def suggest_booking():
    num_seats = int(request.args.get('seat'))
    authorization = request.headers.get('Authorization')
    if authorization != 'Bearer valid_token':
        return 'Invalid token', 401
    available_seats = []
    current_row = None
    for row, seat_bookings in bookings.items():
        available_in_row = []
        for seat, email in seat_bookings.items():
            if len(available_in_row) == num_seats:
                available_seats.append(available_in_row)
                available_in_row = []
            elif len(available_in_row) > 0 and seat_bookings[seat] == '1':
                # If more than 1 seat is requested and a walking path is found, start a new seat group
                available_seats.append(available_in_row)
                available_in_row = []
            elif current_row is not None and current_row != row:
                # If more than 1 seat is requested and a new row is found, start a new seat group
                available_seats.append(available_in_row)
                available_in_row = []
            else:
                available_in_row.append(row + seat)
            current_row = row
        if available_in_row:
            available_seats.append(available_in_row)
    return json.dumps(available_seats)


if __name__ == "__main__":
    app.run(debug=True)
