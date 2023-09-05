from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

from views.openai_view import openai_bp
# from views.trends import serpapi_bp
from views.questions import questions_bp
from views.user import user_bp

from controllers.firebase_controller import Firebase_Controller

from controllers.database import search_user_role

from firebase_admin import auth
from controllers.create_tables import create_connection
from controllers.firebase_controller import Firebase_Controller
# print(firebase_controller.create_user('ishanshrestha@gmail.com', 'testpassword123'))

app = Flask(__name__)
CORS(app)  # Enable CORS for all origins. Replace with specific origins if needed.

app.register_blueprint(openai_bp)
# app.register_blueprint(serpapi_bp)
app.register_blueprint(questions_bp)
app.register_blueprint(user_bp)

@app.route("/")
def read_root():
    return jsonify({"Backend": "Online!!!"})


@app.route('/search')
def search():
    uid = request.args.get('uid')
    if uid:
        role = search_user_role(uid)
        if role:
            return jsonify({'uid': uid, 'role is ': role})
        else:
            return jsonify({'error' : "User not found"})
    else:
        return jsonify({'Error' : 'Missing uid parameter'})
    

firebase_controller = Firebase_Controller()

@app.route('/delete_user', methods=['DELETE'])
def delete_user():
    user_id = request.args.get('user_id')
    token = request.args.get('token')

    # Verify the ID token
    token_verification = firebase_controller.verify_id_token(token)
    if token_verification['status'] == 'Error':
        return jsonify(token_verification)

    # Delete the user from Firebase
    try:
        auth.delete_user(user_id)
    except auth.AuthError as e:
        return jsonify({
            "status": "Error",
            "message": f"An error occurred while deleting the user from Firebase: {e}"
        })

    # Delete the user from the MySQL database
    connection = create_connection()
    cursor = connection.cursor()
    query = f"DELETE FROM application_users WHERE u_id = '{user_id}'"
    try:
        cursor.execute(query)
        connection.commit()
        return jsonify({
            "status": "Success",
            "message": "User deleted successfully from Firebase and MySQL database"
        })
    except Error as e:
        return jsonify({
            "status": "Error",
            "message": f"An error occurred while deleting the user from the MySQL database: {e}"
        })
    



if __name__ == "__main__":
    app.run()
