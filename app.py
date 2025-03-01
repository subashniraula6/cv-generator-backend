from flask import Flask, request, jsonify
#from flask_cors import CORS
from dotenv import load_dotenv
from config import Config
from models.kneg_models import db

from routes.openai_routes import openai_bp
# from routes.trends import serpapi_bp
from routes.questions import questions_bp
from routes.user import user_bp
from routes.kneg_routes import kneg_bp

from controllers.firebase_controller import Firebase_Controller
# from controllers.database import search_user_role

from firebase_admin import auth
# from controllers.create_tables import create_connection
from controllers.firebase_controller import Firebase_Controller
from mysql.connector import Error
import secrets 
# print(firebase_controller.create_user('ishanshrestha@gmail.com', 'testpassword123'))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = Config.mySQL_alchemy_config()['DATABASE_URI']
db.init_app(app)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

 # Create all tables in database. Comment after first time use
# with app.app_context():
#    print(app.app_context())
#    db.create_all()

#CORS(app)  # Enable CORS for all origins. Replace with specific origins if needed.

app.register_blueprint(openai_bp)
# app.register_blueprint(serpapi_bp)
app.register_blueprint(questions_bp)
app.register_blueprint(user_bp)
app.register_blueprint(kneg_bp)

@app.route("/")
def read_root():
    return jsonify({"Backend": "Online!!!"})

@app.route('/get_test_token', methods=['GET'])
def get_test_token():
    # Generate a random token (for demonstration purposes)
    random_token = secrets.token_hex(16)  # Generates a 32-character hexadecimal token
    return jsonify({"token": random_token})


# @app.route('/search')
# def search():
#     uid = request.args.get('uid')
#     if uid:
#         role = search_user_role(uid)
#         if role:
#             return jsonify({'uid': uid, 'role is ': role})
#         else:
#             return jsonify({'error' : "User not found"})
#     else:
#         return jsonify({'Error' : 'Missing uid parameter'})
    

firebase_controller = Firebase_Controller()

# @app.route('/delete_user', methods=['DELETE'])
# def delete_user():
#     print("page delete_user")
#     user_id = request.args.get('user_id')
#     token = request.args.get('token')

#     # Verify the ID token
#     token_verification = firebase_controller.verify_id_token(token)
#     if token_verification['status'] == 'Error':
        
#         return jsonify(token_verification)

#     # Delete the user from Firebase
#     try:
#         auth.delete_user(user_id)
#     except auth.AuthError as e:
#         print("error deleting")
#         return jsonify({
#             "status": "Error",
#             "message": f"An error occurred while deleting the user from Firebase: {e}"
#         })
    

#     # Delete the user from the MySQL database
#     connection = create_connection()
#     cursor = connection.cursor()
#     print("Iniciating use Delete")
#     query = f"DELETE FROM application_users WHERE u_id = '{user_id}'"
#     try:
#         cursor.execute(query)
#         connection.commit()
#         print("deletion success")
#         return jsonify({
#             "status": "Success",
#             "message": "User deleted successfully from Firebase and MySQL database"
#         })
#     except Error as e:
#         print("Error aayo muji")
#         return jsonify({
#             "status": "Error",
#             "message": f"An error occurred while deleting the user from the MySQL database: {e}"
#         })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
