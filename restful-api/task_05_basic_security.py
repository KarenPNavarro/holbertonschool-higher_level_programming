#!/usr/bin/python3
"""Flask API with Basic Auth and JWT authentication."""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (JWTManager, create_access_token,
                                jwt_required, get_jwt_identity)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret-key"

auth = HTTPBasicAuth()
jwt = JWTManager(app)

users = {
    "user1": {"username": "user1",
              "password": generate_password_hash("password"),
              "role": "user"},
    "admin1": {"username": "admin1",
               "password": generate_password_hash("password"),
               "role": "admin"}
}


@auth.verify_password
def verify_password(username, password):
    """Verify username and password for basic auth."""
    if username in users:
        if check_password_hash(users[username]["password"], password):
            return username
    return None


@auth.error_handler
def basic_auth_error(status):
    """Handle basic auth errors."""
    return jsonify({"error": "Unauthorized"}), 401


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """Route protected by basic authentication."""
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    """Login route that returns a JWT token."""
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username not in users:
        return jsonify({"error": "Invalid credentials"}), 401
    if not check_password_hash(users[username]["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(identity=username)
    return jsonify({"access_token": access_token})


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """Route protected by JWT authentication."""
    return "JWT Auth: Access Granted"


@app.route("/admin-only")
@jwt_required()
def admin_only():
    """Route accessible only to admin users."""
    username = get_jwt_identity()
    if users[username]["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


@jwt.unauthorized_loader
def handle_unauthorized(error):
    """Handle missing JWT token."""
    return jsonify({"error": "Unauthorized"}), 401


@jwt.invalid_token_loader
def handle_invalid_token(error):
    """Handle invalid JWT token."""
    return jsonify({"error": "Unauthorized"}), 401


@jwt.expired_token_loader
def handle_expired_token(jwt_header, jwt_payload):
    """Handle expired JWT token."""
    return jsonify({"error": "Unauthorized"}), 401


if __name__ == "__main__":
    app.run()
