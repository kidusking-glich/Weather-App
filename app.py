from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "7d1f1"

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    error = None

    if request.method == "POST":
        city = request.form["city"]
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()
        
        if str(data.get("cod")) == "200":
            weather = {
                "city": city,
                "temp": data["main"]["temp"],
                "description": data["weather"][0]["description"],
                "icon": data["weather"][0]["icon"],
                "humidity": data["main"]["humidity"],
                "wind": data["wind"]["speed"],
                "country": data["sys"]["country"],
                "feels_like": data["main"]["feels_like"]
            }
            if "rain" in weather["description"]:
                bg = "bg-primary"
            elif "clear" in weather["description"]:
                bg = "bg-warning" 
        else:
            error = data.get("message", "City not found.").capitalize()

    return render_template("index.html", weather=weather, error=error)
if __name__ == "__main__":
    app.run(debug=True)
