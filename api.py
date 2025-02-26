import os
import json
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from chat_medical import Chat

app = Flask(__name__)
CORS(app)
chat = Chat()
API_KEYS = {"user1": "hi", "user2": "bye"}

# File path for storing chat history
CHAT_HISTORY_FILE = "chat_history.json"

# Function to read chat history from a file
def load_chat_history():
    if os.path.exists(CHAT_HISTORY_FILE):
        with open(CHAT_HISTORY_FILE, "r") as file:
            return json.load(file)
    return []

# Function to save chat history to a file
def save_chat_history(chat_history):
    with open(CHAT_HISTORY_FILE, "w") as file:
        json.dump(chat_history, file)

@app.route("/")
def home():
    return render_template("index.html")

# Verify the API Key function
def verify_api_key():
    api_key = request.headers.get("X-API-Key")
    if api_key not in API_KEYS.values():
        return jsonify({"error": "Invalid API Key"}), 401
    return None

@app.route("/chat", methods=["POST"])
def chat_response():
    auth = verify_api_key()
    if auth:  
        return auth  # Return 401 if unauthorized
    
    data = request.get_json()
    r = chat.ans(data["query"])
    return jsonify({"response": r}), 200


if __name__ == "__main__":
    app.run(debug=True)