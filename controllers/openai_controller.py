import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=gemini_api_key)

if gemini_api_key is None:
    raise ValueError(
        "GEMINI_API_KEY environment variable not found. Please set it in the .env file."
    )

model = genai.GenerativeModel("gemini-pro")

def get_openai_response(prompt: str) -> str:
    try:
        response = model.generate_content(prompt) # Correct method

        # Check for safety issues
        if response.prompt_feedback and response.prompt_feedback.block_reason:
            return f"Blocked due to safety reasons: {response.prompt_feedback.block_reason}"

        # Extract generated text from the first part
        if response.parts and len(response.parts) > 0:
            return response.parts[0].text.strip()
        else:
            return "No text generated."

    except Exception as e:
        return str(e)