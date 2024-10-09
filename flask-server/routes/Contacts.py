from flask import Blueprint, jsonify
from extensions import db
from models.Contacts import Contacts

contacts_bp = Blueprint("contacts", __name__)

@contacts_bp.get("/")
def get_contacts():
    contacts_list = Contacts.query.all()
    data = [ contacts.to_dict() for contacts in contacts_list]
    return jsonify(data)

@contacts_bp.get("/<id>")
def get_specific_contacts(id):
    filtered_contacts = Contacts.query.get(id)
    if filtered_contacts is None:
        return jsonify({"Message": f"contacts group not found with id: {id}"}), 404
    return jsonify(filtered_contacts.to_dict())
