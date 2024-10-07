from flask import Blueprint, jsonify
from extensions import db
from models.CommunicationStyle import CommunicationStyle

CommunicationStyle_bp = Blueprint("CommunicationStyle", __name__)

@CommunicationStyle_bp.get("/")
def get_CommunicationStyle():
    CommunicationStyle_list = CommunicationStyle.query.all()
    data = [ CommunicationStyle.to_dict() for CommunicationStyle in CommunicationStyle_list]
    return jsonify(data)

@CommunicationStyle_bp.get("/<id>")
def get_specific_CommunicationStyle(id):
    filtered_CommunicationStyle = CommunicationStyle.query.get(id)
    if filtered_CommunicationStyle is None:
        return jsonify({"Message": f"Communication Style not found with id: {id}"}), 404
    return jsonify(filtered_CommunicationStyle.to_dict())
