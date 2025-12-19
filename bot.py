from flask import Flask, request
import requests
import os

TOKEN = os.getenv("BOT_TOKEN")     # read secret token from environment variable
URL = f"https://api.telegram.org/bot{TOKEN}/"

app = Flask(__name__)

def send_message(chat_id, text):
    """Sends a reply back to telegram user"""
    requests.post(URL + "sendMessage", data={"chat_id": chat_id, "text": text})

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()

    chat_id = data["message"]["chat"]["id"]
    text = data["message"]["text"]

    # simple processing: reverse text
    reversed_text = text[::-1]

    send_message(chat_id, f"Reversed: {reversed_text}")
    return "OK"

@app.route("/", methods=["GET"])
def index():
    return "Bot is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
