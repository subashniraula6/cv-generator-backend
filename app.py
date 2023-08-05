from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
import openai

from serpapi_custom import keyword_trend

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
pass_phrase = os.getenv("PASSWORD")

all_engines = ["text-davinci-003", "text-curie-001", "text-babbage-001", "text-ada-001"]

if openai.api_key is None:
    raise ValueError("OPENAI_API_KEY environment variable not found. Please set it in the .env file.")

app = Flask(__name__)
CORS(app)  # Enable CORS for all origins. Replace with specific origins if needed.

@app.route("/")
def read_root():
    return jsonify({"Backend": "Online!!!"})

@app.route("/chat", methods=["POST"])
def read_chat():
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

@app.route("/trends", methods=["POST"])
def get_trends():
    result = keyword_trend('volcano')
    return jsonify({"keyword": 'volcano', "response": result})


def get_openai_response(engine: str, prompt: str) -> str:
    try:
        response = openai.Completion.create(engine=engine, prompt=prompt, max_tokens=2049, temperature=0.7, n=1, stop=None)
        return response.choices[0].text.strip()
    except Exception as e:
        return "Error calling OpenAI API", 500

if __name__ == "__main__":
    app.run()
