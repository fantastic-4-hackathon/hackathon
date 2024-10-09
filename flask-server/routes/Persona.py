from flask import Blueprint, jsonify
from extensions import db
from models.Persona import Persona
from models.Age import Age
from models.Education import Education

Persona_bp = Blueprint("Persona", __name__)

@Persona_bp.get("/")
def get_personas():
    persona_list = Persona.query.all()
    data = [ persona.to_dict() for persona in persona_list]
    return jsonify(data)

@Persona_bp.get("/<id>")
def get_specific_personas(id):
    filtered_persona = Persona.query.get(id)
    if filtered_persona is None:
        return jsonify({"Message": f"Persona not found with id: {id}"}), 404
    age = Age.query.get(filtered_persona.age_range_id)
    if age is None:
        return jsonify({"Message": f"Persona Age not found with id: {filtered_persona.age_range_id}"}), 404
    education = Education.query.get(filtered_persona.education_id)
    if education is None:   
        return jsonify({"Message": f"Persona Education not found with id: {filtered_persona.education_id}"}), 404
    return jsonify({"persona":filtered_persona.to_dict(),"age":age.to_dict(),"education":education.to_dict()}), 200

