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
    prompt = request_data.get("prompt")

    response = get_openai_response(prompt)
    return jsonify({"prompt": prompt, "response": response})

