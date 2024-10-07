from flask import Blueprint, request, jsonify
from models.user import User
from extensions import db, bcrypt, jwt
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

auth_bp = Blueprint('auth', __name__)

# Register for now (to create dummy users perhaps and check hashing)
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'User already exists'}), 400

    # Hash password
    password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    # Create new user
    new_user = User(username=username, password_hash=password_hash)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'}), 201


# login (no register in production)
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Find user by username
    user = User.query.filter_by(username=username).first()

    if user and bcrypt.check_password_hash(user.password_hash, password):
        # Create access token
        access_token = create_access_token(identity={'username': user.username})
        return jsonify({'access_token': access_token}), 200
    else:
        return jsonify({'error': 'Invalid username or password'}), 401

# protected dummy route
@auth_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify({'message': f'Hello {current_user["username"]}, you are accessing a protected route.'})