
import json
from flask import request, jsonify, Blueprint
from controllers.firebase_controller import Firebase_Controller
from controllers.kneg_ORM_controller import createOrLoginUser

user_bp = Blueprint('user', __name__)

firebase = Firebase_Controller()

@user_bp.route('/test', methods=['POST'])
def test():
    return jsonify({"active": "yes"})

@user_bp.route('/signup', methods=['POST'])
def signup():
    try:
        data = request.json
        email = data.get("email")
        password = data.get("password")
        response = firebase.create_user(email,password)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@user_bp.route('/delete_user', methods=['POST'])
def delete_user():
    try:
        data = request.json
        user_id = data.get("user_id")
        # token = data.get("token")
        if firebase.delete_user(user_id):
            return jsonify({"success": "User deleted successfully"}), 200
        return jsonify({"error": "An error Occurred while deleting user."}), 500
    except Exception as e: 
        print(e)
        return jsonify({"error": "An error Occurred while deleting user."}), 500
        

@user_bp.route('/test_delete_user', methods=['POST'])
def test_delete_user():
    # try:
    data = request.json
    uid = data.get("uid")
    # token = data.get("token")
    if firebase.test_delete_user(uid):
        return jsonify({"success": "User deleted successfully"}), 200
    return jsonify({"error": "An error Occurred while deleting user."}), 500
    # except Exception as e: 
    #     print(e)
    #     return jsonify({"error": "An error Occurred while deleting user."}), 500
        
@user_bp.route('/createOrLogin', methods=['POST'])
def createOrLogin():
    data = request.json
    email = data.get("email")
    uid = data.get("uid")
    isCreated = createOrLoginUser(email, uid)
    if isCreated:
        return jsonify({"success": "User created successfully"}), 200
    return jsonify({"success": "User already exist"}), 200