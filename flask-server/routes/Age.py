from flask import Blueprint, jsonify
from extensions import db
from models.Age import Age

age_bp = Blueprint("age", __name__)

@age_bp.get("/")
def get_age():
    age_list = Age.query.all()
    data = [ age.to_dict() for age in age_list]
    return jsonify(data)

@age_bp.get("/<id>")
def get_specific_age(id):
    filtered_age = Age.query.get(id)
    if filtered_age is None:
        return jsonify({"Message": f"Age not found with id: {id}"}), 404
    return jsonify(filtered_age.to_dict())
