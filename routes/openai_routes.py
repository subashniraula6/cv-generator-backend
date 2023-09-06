import os
from dotenv import load_dotenv
from flask import request, jsonify, Blueprint

from controllers.openai_controller import get_openai_response


pass_phrase = os.getenv("PASSWORD")
all_engines = ["text-davinci-003", "text-curie-001", "text-babbage-001", "text-ada-001"]

openai_bp = Blueprint('openai', __name__)

@openai_bp.route('/openai')
def profile():
    return jsonify({"status": "active"})


@openai_bp.route("/chat", methods=["POST"])
def get_result():
    request_data = request.get_json()
    prompt = request_data.get("prompt", "")
    engine = request_data.get("engine", "text-davinci-003")
    
    # So that garbage from frontend doesn't pass ahead
    if engine not in all_engines:
        engine = "text-davinci-003"

    password = request_data.get("password","")
    if password != pass_phrase: 
        return jsonify({"Error":"Incorrect Key"})

    response = get_openai_response(engine, prompt)
    return jsonify({"prompt": prompt, "response": response})

