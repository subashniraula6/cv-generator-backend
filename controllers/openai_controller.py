import os
import openai
from dotenv import load_dotenv
from config import Config
load_dotenv()

CONFIG = Config.openAI_config()
openai.api_key = CONFIG['API_KEY']
if openai.api_key is None:
    raise ValueError("OPENAI_API_KEY environment variable not found. Please set it in the .env file.")

def get_openai_response(engine: str, prompt: str) -> str:
    print(f"here is confgi {CONFIG} & {CONFIG['API_KEY']}")

    try:
        response = openai.Completion.create(engine=engine, prompt=prompt, max_tokens=2049, temperature=0.7, n=1, stop=None)
        return response.choices[0].text.strip()
    except Exception as e:
        return "Error calling OpenAI API", 500
