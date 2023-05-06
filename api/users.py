from flask import request, url_for,jsonify,json,Blueprint
import requests
from api import db
from werkzeug.security import check_password_hash
from api.models import *
from api.auth import create_auth_token

users = Blueprint('users', __name__)

@users.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    print(data)
    if not data:
        return jsonify({'msg': 'Missing JSON'}), 400

    user = User(**data)
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'user created successfully'})


@users.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data:
        return jsonify({'msg': 'Missing JSON'}), 400

    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'error': 'Invalid credentials'}), 400

    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({'error': 'Invalid email'}), 401

    if not user.verify_password(password):
        return jsonify({'error': 'Invalid password'}), 401

    # User is authenticated, return success response
    token = create_auth_token(user.id)
    return jsonify({'message': 'Login successful', 'user_id': user.id,'token': token}), 200
 


