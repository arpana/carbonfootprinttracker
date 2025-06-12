from flask import Flask, request, jsonify
from services.user_service import UserService
from models.users import User

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask!"

@app.route("/register", methods=["POST"])
def register():
    data = request.json
    if not all(k in data for k in ("email", "password")):
        return jsonify({"error": "Missing email or password"}), 400

    user = User(email=data["email"], password=data["password"])
    success, message = UserService.register(user)
    return jsonify({"message": message}), 201 if success else 400

''''curl -X POST http://127.0.0.1:8000/login \
     -H "Content-Type: application/json" \
     -d '{"email": "arpanachopra80@gmail.com", "password": "Technology1!"}' '''
@app.route("/login", methods=["POST"])
def login():
    data = request.json
    if not all(k in data for k in ("email", "password")):
        return jsonify({"error": "Missing email or password"}), 400

    success, message = UserService.login(data["email"], data["password"])
    return jsonify({"message": message}), 200 if success else 401


@app.route("/forgot-password", methods=["POST"])
def forgot_password():
    data = request.json
    if not all(k in data for k in ("email", "new_password")):
        return jsonify({"error": "Missing email or new_password"}), 400

    success, message = UserService.update_password(data["email"], data["new_password"])
    return jsonify({"message": message}), 200 if success else 400


if __name__ == "__main__":
    app.run(debug=True)
