from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

RASA_URL = "http://localhost:5005/chatbot/webhooks/rest/webhook"

@app.route('/check')
def check():
    return render_template('check.html')

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

@app.route("/chatbot/webhook", methods=["POST"])
def webhook():
    user_message = request.json.get("message")
    payload = {"sender": "user", "message": user_message}
    response = requests.post(RASA_URL, json=payload)
    bot_messages = response.json()
    return jsonify(bot_messages)

@app.route('/team')
def team():
    return render_template('team.html')

if __name__ == "__main__":
    app.run(port=5000)
