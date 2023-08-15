from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

from views.openai_view import openai_bp
from views.trends import serpapi_bp
from views.questions import questions_bp
from views.user import user_bp

from controllers.firebase_controller import Firebase_Controller

# print(firebase_controller.create_user('ishanshrestha@gmail.com', 'testpassword123'))

app = Flask(__name__)
CORS(app)  # Enable CORS for all origins. Replace with specific origins if needed.

app.register_blueprint(openai_bp)
app.register_blueprint(serpapi_bp)
app.register_blueprint(questions_bp)
app.register_blueprint(user_bp)

@app.route("/")
def read_root():
    return jsonify({"Backend": "Online!!!"})

if __name__ == "__main__":
    app.run()
