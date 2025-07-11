import os
import google.generativeai as genai
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

app = Flask(__name__)
# Allow requests from your frontend (HTML file opened in browser)
CORS(app)

# --- Configure Gemini API ---
try:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in .env file or environment variables.")
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.0-flash')
except Exception as e:
    print(f"Error configuring Gemini: {e}")
    model = None

# --- Helper Functions ---
def construct_story_prompt(topic, genres):
    prompt = f'Write a short story about "{topic}".'
    if genres:
        prompt += f' The story should be a blend of the following genres: {", ".join(genres)}.'
    prompt += " The story should be engaging, well-structured, and have a clear beginning, middle, and end."
    return prompt

def construct_certification_prompt(story, board):
    board_map = {
        'MPA': 'MPA (Motion Picture Association of America)',
        'CBFC': 'CBFC (Central Board of Film Certification, India)',
        'BBFC': 'BBFC (British Board of Film Classification)'
    }
    full_name = board_map.get(board, board)
    return f'Based on the official guidelines of the {full_name}, analyze the following story. First, provide ONLY the suitable age rating on its own line in the format "{board}: [Rating]" (e.g., "CBFC: U/A"). Then, on a new line, start with "Reasons:" followed by a brief, one or two-sentence explanation for the rating. Story: "{story}"'

def call_gemini_api(prompt):
    if not model:
        return "Error: Gemini model not initialized.", False
    try:
        response = model.generate_content(prompt)
        return response.text, True
    except Exception as e:
        print(f"Gemini API Error: {e}")
        # Try to provide a more specific error message if available
        if "API key not valid" in str(e):
            return "Error: Your Gemini API key is not valid. Please check your .env file.", False
        return f"Error: An issue occurred while contacting the AI model: {e}", False

# --- API Routes ---
@app.route('/generate', methods=['POST'])
def generate_story_and_certify():
    data = request.get_json()
    topic = data.get('topic')
    genres = data.get('genres')
    board = data.get('board')

    if not all([topic, genres, board]):
        return jsonify({"error": "Missing required fields: topic, genres, or board."}), 400

    # 1. Generate Story
    story_prompt = construct_story_prompt(topic, genres)
    story, success = call_gemini_api(story_prompt)
    if not success:
        return jsonify({"error": story}), 500

    # 2. Generate Certification
    cert_prompt = construct_certification_prompt(story, board)
    certification, success = call_gemini_api(cert_prompt)
    if not success:
        # Still return the story even if certification fails
        return jsonify({"story": story, "certification": "Could not generate rating."})

    return jsonify({"story": story, "certification": certification})

@app.route('/certify', methods=['POST'])
def certify_story():
    data = request.get_json()
    story = data.get('story')
    board = data.get('board')

    if not all([story, board]):
        return jsonify({"error": "Missing required fields: story or board."}), 400

    cert_prompt = construct_certification_prompt(story, board)
    certification, success = call_gemini_api(cert_prompt)
    if not success:
        return jsonify({"error": certification}), 500

    return jsonify({"certification": certification})

if __name__ == '__main__':
    app.run(debug=True)