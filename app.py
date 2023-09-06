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

# from controllers.database import search_user_role
# print(firebase_controller.create_user('ishanshrestha@gmail.com', 'testpassword123'))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = Config.mySQL_alchemy_config()['DATABASE_URI']
db.init_app(app)
with app.app_context():
    print(app.app_context())
    db.create_all()
CORS(app)  # Enable CORS for all origins. Replace with specific origins if needed.

app.register_blueprint(openai_bp)
# app.register_blueprint(serpapi_bp)
app.register_blueprint(questions_bp)
app.register_blueprint(user_bp)
app.register_blueprint(kneg_bp)

@app.route("/")
def read_root():
    return jsonify({"Backend": "Online!!!"})


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
    

if __name__ == "__main__":
    app.run()
