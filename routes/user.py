
import json
from flask import request, jsonify, Blueprint
from controllers.firebase_controller import Firebase_Controller

user_bp = Blueprint('user', __name__)

firebase = Firebase_Controller()

@user_bp.route('/test', methods=['POST'])
def test():
    return jsonify({"active": "yes"})

@user_bp.route('/signup', methods=['POST'])
def get_trends():
    try:
        data = request.json
        email = data.get("email")
        password = data.get("password")
        response = firebase.create_user(email,password)
        print(response)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
