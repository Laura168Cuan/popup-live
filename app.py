from flask import Flask, jsonify
from flask_cors import CORS
import requests
from datetime import datetime

app = Flask(__name__)
CORS(app)

API_KEY = "75a8477ac2339ea7c5642901a1e073d4"
HEADERS = {"x-apisports-key": API_KEY}

@app.route("/")
def home():
    return jsonify({
        "status": "ok",
        "message": "Live Score API aktif",
        "available_routes": ["/fixtures/today"]
    })

@app.route("/fixtures/today")
def fixtures_today():
    today = datetime.now().strftime('%Y-%m-%d')
    url = f"https://v3.football.api-sports.io/fixtures?date={today}"
    try:
        res = requests.get(url, headers=HEADERS, timeout=10)
        res.raise_for_status()
        return jsonify(res.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500
