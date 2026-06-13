#!/usr/bin/python3
"""Simple API using Flask."""
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route("/")
def home():
    """Return welcome message."""
    return "Welcome to the Flask API!"


@app.route("/status")
def status():
    """Return API status."""
    return "OK"


@app.route("/data")
def data():
    """Return list of all usernames."""
    return jsonify(list(users.keys()))


@app.route("/users/<username>")
def get_user(username):
    """Return full object for a given username."""
    if username in users:
        return jsonify(users[username])
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user to the API."""
    data = request.get_json()

    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400
    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400
    if data["username"] in users:
        return jsonify({"error": "Username already exists"}), 409

    username = data["username"]
    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run()
