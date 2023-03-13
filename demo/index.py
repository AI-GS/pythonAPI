from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {'name': 'Sai', 'address': 'Toronto'}
]


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/users")
def get_users():
    return jsonify(users)


@app.route("/users", methods=['POST'])
def add_user():
    users.append(request.get_json())
    return '', 204
