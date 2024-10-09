from flask import Blueprint, jsonify, request
from extensions import db
from models.user import User

Persona_bp = Blueprint("Persona", __name__)

@Persona_bp.route("/login", methods=["GET", "POST"])
def login():
    body = request.get_json()
    user = User.query.filter_by(user_Ecode=body.user_Ecode).first()
    return jsonify(user)

