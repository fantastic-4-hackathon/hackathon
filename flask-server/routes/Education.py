from flask import Blueprint, jsonify
from extensions import db
from models.Education import Education

education_bp = Blueprint("education", __name__)

@education_bp.get("/")
def get_education():
    education_list = Education.query.all()
    data = [ education.to_dict() for education in education_list]
    return jsonify(data)

@education_bp.get("/<id>")
def get_specific_education(id):
    filtered_education = Education.query.get(id)
    if filtered_education is None:
        return jsonify({"Message": f"Education group not found with id: {id}"}), 404
    return jsonify(filtered_education.to_dict())
