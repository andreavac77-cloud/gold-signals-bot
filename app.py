import os
import requests
from flask import Flask, request

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

@app.route("/", methods=["POST"])
def webhook():
    data = request.json
    if not data:
        return "No data", 400

    action = data.get("action", "SIGNAL")
    price = data.get("price", "")
    sl = data.get("sl", "")
    tp1 = data.get("tp1", "")
    tp2 = data.get("tp2", "")

    message = (
        f"🚨 **GOLD SIGNAL (XAUUSD)** 🚨\n\n"
        f"📊 Azione: **{action}**\n"
        f"💰 Entrata: `{price}`\n"
        f"🛑 Stop Loss: `{sl}`\n"
        f"🎯 Take Profit 1: `{tp1}`\n"
        f"🎯 Take Profit 2: `{tp2}`\n"
        f"⏱ Timeframe: M15"
    )

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }

    requests.post(url, json=payload)
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
