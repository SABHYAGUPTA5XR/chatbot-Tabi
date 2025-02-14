from flask import Flask, request, jsonify, render_template
import os
from mistralai import Mistral
from dotenv import load_dotenv

# Load environment variables from a .env file if available
load_dotenv()

app = Flask(__name__)

# Retrieve the Mistral API key from the environment
api_key = os.getenv("MISTRAL_API_KEY")
if not api_key:
    raise ValueError("Please set the MISTRAL_API_KEY environment variable.")

# Define the model name
model = "mistral-large-latest"

# Initialize the Mistral client
client = Mistral(api_key=api_key)

def chat_with_mistral(query):
    # Use the Mistral API to generate a response
    chat_response = client.chat.complete(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "system", "content": "You are a friendly assistant named Tabi. When a user says 'Thanks', 'Bye', or 'Okay', reply with a concise and varied response such as 'Happy to help!' or 'I'm here if you need anything.' Avoid long, repetitive responses."},
            {"role": "user", "content": "Thanks"},
            {"role": "assistant", "content": "Happy to help!"},
            {"role": "user", "content": "Bye"},
            {"role": "assistant", "content": "Take care! I'm here whenever you need me."},
            {"role": "user", "content": query},
        ]
    )
    return chat_response.choices[0].message.content

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get("message", "")
    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    try:
        reply = chat_with_mistral(user_input)
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
