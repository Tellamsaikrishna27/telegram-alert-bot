from flask import Flask, request, jsonify
import requests, os

app = Flask(name)

TELEGRAM_TOKEN = os.getenv("8335068411:AAHR_T2P2JgdNHWf00D_77jbFF-udlWsE3g") 
TELEGRAM_CHAT_ID = os.getenv("5069236323") 
def send_telegram(msg):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": msg}
    requests.post(url, json=payload)

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()
    msg = (
        f"📢 Alert Triggered\n\n"
        f"Symbol: {data.get('symbol')}\n"
        f"Side: {data.get('side')}\n"
        f"Price: {data.get('price')}\n"
        f"SL: {data.get('sl')}\n"
        f"TP: {data.get('tp')}\n"
        f"{data.get('comment','')}"
    )
    send_telegram(msg)
    return jsonify({"ok": True})
