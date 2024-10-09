from flask import Blueprint, jsonify, request
from extensions import bcrypt
from models.user import User

user_bp = Blueprint("user", __name__)


@user_bp.route("/login", methods=["GET", "POST"])
def login():
    body = request.get_json()
    print(body)
    user = User.query.filter_by(user_Ecode=body["user_Ecode"]).first()
    if user:
        if bcrypt.check_password_hash(user.password_hash, body["password"]):
            return jsonify(
                {
                    "message": "Success",
                    "user_id": user.id,
                    "name": user.user_name,
                    "surname": user.user_lastname,
                }
            )
        else:
            return jsonify({"message": "Failed: Invalid Ecode/password"}), 401
    else:
        return jsonify({"message": "Failed: Invalid Ecode/password"}), 401
