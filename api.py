from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from chat import Chat


app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat_response():
  data = request.get_json()

  chat = Chat()
  r = chat.ans(data["query"])
  data['response'] = r
  return jsonify(data), 200

if __name__ == "__main__":
  app.run(debug=True)