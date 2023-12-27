from flask import Blueprint, request, jsonify
from controllers.user_controller import create_new_user
from controllers.user_controller import get_all_users
from controllers.user_controller import authenticate_user
from utilities.token_util import generate_token

user_blueprint = Blueprint('user_blueprint', __name__)

@user_blueprint.route('/login', methods=['POST'])
def login():
    user_data = request.json
    email = user_data['email']
    password = user_data['password']

    user = authenticate_user(email, password)
    if user:
        token = generate_token(user['id'])
        return jsonify({'token': token}), 200
    else:
        return jsonify({'error': 'Invalid credentials'}), 401


@user_blueprint.route('/create_user', methods=['POST'])
def create_user():
    user_data = request.json
    email = user_data['email']
    username = user_data['username']
    if create_new_user(email, username):
        return jsonify({'message': 'User created successfully'}), 201
    else:
        return jsonify({'error': 'Failed to create user'}), 500


@user_blueprint.route('/users', methods=['GET'])
def users():
    users = get_all_users()
    return jsonify(users)