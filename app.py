import os
import google.generativeai as genai
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

app = Flask(__name__)
# Allow requests from your frontend
CORS(app)

# --- Configure Gemini API ---
try:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in .env file or environment variables.")
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    print(f"Error configuring Gemini: {e}")
    model = None

# --- Helper Functions ---
def construct_story_prompt(topic, genres, language):
    """Constructs the prompt for the AI to generate a story."""
    prompt_template = f"""You are an expert storyteller for all ages. Your task is to take the user's idea and write a complete, engaging story with a clear beginning, middle, and end.

### User's Story Idea:
"{topic}"

### Story Genres:
The story should be a blend of the following genres: {", ".join(genres)}.

### CRITICAL INSTRUCTION:
You MUST write the entire story ONLY in the **{language}** language. Do not output any English text in the story.
"""
    return prompt_template

def construct_translation_prompt(text, language):
    """Creates a prompt to translate the given text."""
    return f"""Translate the following text into the **{language}** language.
Provide ONLY the translated text and nothing else.

Text to translate:
---
{text}
---
"""

def construct_certification_prompt(story, board):
    """Creates a prompt to get an age rating for a story."""
    board_map = {
        'MPA': 'MPA (Motion Picture Association of America)',
        'CBFC': 'CBFC (Central Board of Film Certification, India)',
        'BBFC': 'BBFC (British Board of Film Classification)',
        'MRO': 'MRO (Media Regulatory Office, UAE)',
        'FSK': 'FSK (Freiwillige Selbstkontrolle der Filmwirtschaft, Germany)',
        'EIRIN': 'EIRIN (Film Classification and Rating Organization, Japan)',
        'CNC': 'CNC (Centre national du cinéma et de l\'image animée, France)',
        'IMDA': 'IMDA (Info-communications Media Development Authority, Singapore)',
        'ACB': 'ACB (Australian Classification Board, Australia)',
        'KAVI': 'KAVI (National Audiovisual Institute, Finland)'
    }
    full_name = board_map.get(board, board)
    return f'Based on the official guidelines of the {full_name}, analyze the following story. First, provide ONLY the suitable age rating on its own line in the format "{board}: [Rating]" (e.g., "CBFC: U/A"). Then, on a new line, start with "Reasons:" followed by a brief, one or two-sentence explanation for the rating. Story: "{story}"'

def call_gemini_api(prompt):
    """Calls the Gemini API and handles errors."""
    if not model:
        return "Error: Gemini model not initialized.", False
    try:
        response = model.generate_content(prompt)
        return response.text, True
    except Exception as e:
        print(f"Gemini API Error: {e}")
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
    language = data.get('language', 'English')

    if not all([topic, genres, board, language]):
        return jsonify({"error": "Missing required fields: topic, genres, board, or language."}), 400

    story_prompt = construct_story_prompt(topic, genres, language)
    story, success = call_gemini_api(story_prompt)
    if not success:
        return jsonify({"error": story}), 500
    
    cert_prompt = construct_certification_prompt(story, board)
    certification, success = call_gemini_api(cert_prompt)
    if not success:
        return jsonify({"story": story, "certification": "Could not generate rating."})

    return jsonify({"story": story, "certification": certification})

@app.route('/translate', methods=['POST'])
def translate_story():
    data = request.get_json()
    story_text = data.get('story')
    language = data.get('language')

    if not all([story_text, language]):
        return jsonify({"error": "Missing required fields: story or language."}), 400

    translation_prompt = construct_translation_prompt(story_text, language)
    translated_text, success = call_gemini_api(translation_prompt)
    if not success:
        return jsonify({"error": translated_text}), 500

    return jsonify({"translated_story": translated_text})

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
