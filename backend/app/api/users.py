from flask import Blueprint, request, jsonify

from app.database.db import db
from app.models.user import User


users_bp = Blueprint("users", __name__)


@users_bp.route("/api/users", methods=["POST"])
def create_user():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body is required"}), 400

    name = data.get("name")
    email = data.get("email")
    role = data.get("role", "user")

    if not name or not email:
        return jsonify({"error": "Name and email are required"}), 400

    existing_user = User.query.filter_by(email=email).first()

    if existing_user:
        return jsonify({"error": "User with this email already exists"}), 409

    user = User(
        name=name,
        email=email,
        role=role
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({
        "message": "User created successfully",
        "user": {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "role": user.role
        }
    }), 201