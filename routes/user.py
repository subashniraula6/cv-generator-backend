
import json
from flask import request, jsonify, Blueprint
from controllers.firebase_controller import Firebase_Controller

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
        print(response)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@user_bp.route('/delete_user', methods=['POST'])
def delete_user():
    try:
        data = request.json
        u_id = data.get("u_id")
        # token = data.get("token")
        if firebase.delete_user(u_id):
            return jsonify({"success": "User deleted successfully"}), 200
    except Exception as e: 
        print(e)
        return jsonify({"error": "An error Occurred while deleting user."}), 500
        