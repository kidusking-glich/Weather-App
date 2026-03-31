from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "62a65fe458eda80787d74aafa387d1f1"

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None

    if request.method == "POST":
        city = request.form["city"]
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)