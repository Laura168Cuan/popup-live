from flask import Flask, jsonify
from flask_cors import CORS
import requests
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Aktifkan CORS untuk semua route

API_KEY = "75a8477ac2339ea7c5642901a1e073d4"
HEADERS = {"x-apisports-key": API_KEY}

@app.route('/fixtures/today')
def fixtures_today():
    today = datetime.now().strftime('%Y-%m-%d')
    url = f'https://v3.football.api-sports.io/fixtures?date={today}'
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        return jsonify({"error": "Gagal mengambil data dari API-Football", "detail": str(e)}), 500
    return jsonify(data)

if __name__ == '__main__':
    # Host 0.0.0.0 supaya bisa diakses dari luar (misal Render.com)
    app.run(host='0.0.0.0', port=5000, debug=True)
