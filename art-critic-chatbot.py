# requirements.txt
random

# Procfile
web: python app.py

# runtime.txt
python-3.9.18

# app.py
import os
from flask import Flask, render_template, request, jsonify
from etienne_bot import EtienneLaFleur

app = Flask(__name__)
bot = EtienneLaFleur()

@app.route('/')
def home():
    return '''
    <html>
        <head>
            <title>Étienne LaFleur - Art Critic Bot</title>
            <style>
                body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
                .chat-box { border: 1px solid #ccc; padding: 20px; margin: 20px 0; }
                input, button { padding: 10px; margin: 5px; }
            </style>
        </head>
        <body>
            <h1>Étienne LaFleur - Art Critic Bot</h1>
            <div class="chat-box">
                <div id="responses"></div>
                <input type="text" id="userInput" placeholder="Ask about art...">
                <button onclick="sendMessage()">Send</button>
            </div>
            <script>
                function sendMessage() {
                    const input = document.getElementById('userInput');
                    const message = input.value;
                    fetch('/chat', {
                        method: 'POST',
                        headers: {'Content-Type': 'application/json'},
                        body: JSON.stringify({message: message})
                    })
                    .then(response => response.json())
                    .then(data => {
                        const responses = document.getElementById('responses');
                        responses.innerHTML += `<p><strong>You:</strong> ${message}</p>`;
                        responses.innerHTML += `<p><strong>Étienne:</strong> ${data.response}</p>`;
                        input.value = '';
                    });
                }
            </script>
        </body>
    </html>
    '''

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message', '').lower()
    
    if 'review' in message:
        response = bot.review_art(message.replace('review', '').strip())
    elif 'history' in message or 'movement' in message:
        response = bot.discuss_art_history(message.replace('history', '').replace('movement', '').strip())
    elif 'recommend' in message:
        response = bot.provide_recommendations(message.replace('recommend', '').strip())
    else:
        response = "Please ask me about art review, art history, or recommendations!"
    
    return jsonify({'response': response})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
