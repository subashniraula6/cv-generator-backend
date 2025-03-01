from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from config import Config
from models.kneg_models import db

from routes.openai_routes import openai_bp
# from routes.trends import serpapi_bp
from routes.questions import questions_bp
from routes.user import user_bp
from routes.kneg_routes import kneg_bp

from controllers.firebase_controller import Firebase_Controller

from firebase_admin import auth
from controllers.firebase_controller import Firebase_Controller
from mysql.connector import Error
import secrets 

app = Flask(__name__)
CORS(app, origins='*')
app.config['SQLALCHEMY_DATABASE_URI'] = Config.mySQL_alchemy_config()['DATABASE_URI']
db.init_app(app)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

app.register_blueprint(openai_bp)
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

firebase_controller = Firebase_Controller()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
