import requests
from flask import Flask, jsonify
import os

app = Flask(__name__)

API_KEY = "eab43705a549b91a643770b4a3ecef7e"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

@app.route('/weather/<city>')
def get_weather(city):
    # API 호출 URL 생성
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
        "lang": "kr"
    }
    # API 요청
    response = requests.get(BASE_URL, params=params)
    # 응답 데이터와 상태 코드 반환
    return response.json(), response.status_code

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)