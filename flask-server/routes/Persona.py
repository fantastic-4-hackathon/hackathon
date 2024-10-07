from flask import Blueprint, jsonify
from extensions import db
from models.Persona import Persona

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
    return jsonify(filtered_persona.to_dict())
