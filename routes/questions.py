import json
from flask import request, jsonify, Blueprint

questions_bp = Blueprint('questions', __name__)

@questions_bp.route('/questions')
def read_json_file():
    try:
        with open("database/questions.json", 'r') as json_file:
            data = json.load(json_file)
            return jsonify({
                "status": "Success",
                "message": "JSON file read successfully",
                "data": data
            })
    except FileNotFoundError:
        return jsonify({
            "status": "Error",
            "message": "File not found"
        })