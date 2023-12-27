from flask import Blueprint, request, jsonify
from controllers.user_controller import create_new_user
from controllers.user_controller import get_all_users
from controllers.user_controller import authenticate_user
from controllers.user_controller import update_user
from utilities.response_util import sendDataResponse, sendMessageResponse
from utilities.token_util import generate_token

user_blueprint = Blueprint('user_blueprint', __name__)

# Get all users
@user_blueprint.route('/get-all-users', methods=['GET'])
def get_all_users_route():
    try:
        foundUsers = get_all_users()
        if not foundUsers:
            return sendMessageResponse('Users not found', 404)  
        
        return sendDataResponse({'Found Users: ': foundUsers}, 200)  
    except Exception as e:
        return sendMessageResponse(str(e), 500) 


# Create a new user  
@user_blueprint.route('/create-new-user', methods=['POST'])
def create_new_user_route():
    try:
        print("hi")
        newCreatedUser = create_new_user()
        print("Created new user: " + newCreatedUser)
        
        if not newCreatedUser:
            return sendMessageResponse('Users not created', 404)  
        
        return sendDataResponse({"message": "User created successfully"}, 201)
    except Exception as e:
        return sendDataResponse("str(e)", 500)
    

@user_blueprint.route('/update-user/<user_id>', methods=['PATCH'])
def update_user_route(user_id):
    user_data = request.json
    if not user_data:
        return sendMessageResponse('No data provided', 400)

    if update_user(user_id, user_data):
        return sendDataResponse({'message': 'User updated successfully'}, 200)
    else:
        return sendMessageResponse('Failed to update user', 500)  
   
   

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


