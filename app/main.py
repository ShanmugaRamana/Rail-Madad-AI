from flask import Flask, render_template, request, jsonify
from app.chatbots import handle_chat
from app.categorization import categorize_complaint
from app.ocr_extraction import extract_text_from_image
from app.sentiment_analysis import analyze_sentiment
from app.routing import route_complaint

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/complaints', methods=['POST'])
def complaints():
    data = request.json
    category = categorize_complaint(data['content'])
    return jsonify({'category': category})

@app.route('/ocr', methods=['POST'])
def ocr():
    image = request.files['image']
    text = extract_text_from_image(image)
    return jsonify({'extracted_text': text})

@app.route('/chat', methods=['POST'])
def chat():
    message = request.json['message']
    response = handle_chat(message)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
