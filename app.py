from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)
chatbot = pipeline("conversational", model="microsoft/DialoGPT-medium")

@app.route('/api/converse', methods=['POST'])
def converse():
    user_input = request.json.get('message')
    conversation = chatbot(user_input)
    response = conversation[0]['generated_text']
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
