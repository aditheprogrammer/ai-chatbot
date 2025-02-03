from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from chat_filtered import Chat


app = Flask(__name__)
CORS(app)
chat = Chat()
API_KEYS = {"user1": "hi", "user2": "bye"}

@app.route("/")
def home():
    return render_template("index.html")

def verify_api_key():
    api_key = request.headers.get("X-API-Key")
    if api_key not in API_KEYS.values():
        return jsonify({"error": "Invalid API Key"}), 401

@app.route("/chat", methods=["POST"])
def chat_response():
  auth = verify_api_key()
  if auth:
      return auth  # Return 401 if unauthorized
  data = request.get_json()

  r = chat.ans(data["query"])
  data['response'] = r
  return jsonify(data), 200

if __name__ == "__main__":
  app.run(debug=True)