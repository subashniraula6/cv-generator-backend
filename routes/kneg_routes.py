import json
from flask import request, jsonify, Blueprint

from controllers.kneg_SQL_controller import add_user_to_db
from models.user_model import db
from config import Config

# Configure

kneg_bp = Blueprint('kneg', __name__)

@kneg_bp.route('/kneg/user', methods=['POST'])
def user_insert():
    print('inside kneg')
    try:
        data = request.json  # Assuming you are sending JSON data in the request body
        print(data)
        email = data.get('email')
        user_fname = data.get('user_fname')
        user_lname = data.get('user_lname')
        u_id = data.get('u_id')

        if email and user_fname and user_lname and u_id:
            # Call the insert_application_users function to insert data into the database
            add_user_to_db(user_fname, email)
            return jsonify({"message": "User data inserted successfully"}), 200
        else:
            return jsonify({"error": "Missing required data"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500