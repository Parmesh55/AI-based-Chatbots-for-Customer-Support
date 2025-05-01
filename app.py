from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS  # Optional: helps avoid cross-domain issues
from response_generator import generate_response
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/chat', methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    response_message = generate_response(user_message)
    return jsonify({
        "response": response_message
    })

@app.route('/')
def serve_index():
    # Serve index.html from the current directory
    return send_from_directory(os.getcwd(), 'index.html')

if __name__ == "__main__":
    app.run(debug=True, port=5000)
