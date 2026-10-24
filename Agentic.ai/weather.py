
from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Weather Report</title>
<style>
* { box-sizing: border-box; }
body {
    margin: 0;
    padding: 20px;
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    font-family: Arial, sans-serif;
    background: linear-gradient(135deg, #74ebd5, #9face6);
    color: #263653;
}
.card {
    width: 100%;
    max-width: 560px;
    background: white;
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0 10px 30px #0002;
}
h1 { text-align: center; margin-bottom: 8px; }
.subtitle { text-align: center; color: #68758a; }
form { display: flex; gap: 10px; margin: 24px 0; }
input {
    flex: 1;
    min-width: 0;
    padding: 13px;
    border: 1px solid #ccd5e0;
    border-radius: 8px;
    font-size: 16px;
}
button {
    padding: 13px 18px;
    border: 0;
    border-radius: 8px;
    color: white;
    background: #365fce;
    cursor: pointer;
    font-size: 15px;
}
button:hover { background: #2447a7; }
.weather {
    text-align: center;
    background: #f0f5ff;
    padding: 20px;
    border-radius: 14px;
}
.temperature {
    font-size: 46px;
    font-weight: bold;
    color: #365fce;
    margin: 12px;
}
.details {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-top: 18px;
}
.item {
    background: white;
    padding: 16px 8px;
    border-radius: 10px;
}
.label { color: #68758a; font-size: 13px; margin-bottom: 8px; }
.value { font-weight: bold; }
.error {
    color: #b42318;
    background: #fff0ee;
    padding: 12px;
    border-radius: 8px;
}
@media(max-width: 420px) {
    form { flex-direction: column; }
}
</style>
</head>
<body>
<div class="card">
    <h1>Weather Report</h1>
    <p class="subtitle">Check the weather in any city</p>

    <form method="POST">
        <input name="city" placeholder="Enter city name"
               value="{{ city }}" required>
        <button type="submit">Search</button>
    </form>

    {% if error %}
        <p class="error">{{ error }}</p>
    {% endif %}

    {% if weather %}
    <div class="weather">
        <h2>{{ weather.city }}</h2>
        <p>{{ weather.condition }}</p>
        <div class="temperature">{{ weather.temperature }}°C</div>

        <div class="details">
            <div class="item">
                <div class="label">Feels Like</div>
                <div class="value">{{ weather.feels }}°C</div>
            </div>
            <div class="item">
                <div class="label">Humidity</div>
                <div class="value">{{ weather.humidity }}%</div>
            </div>
            <div class="item">
                <div class="label">Wind Speed</div>
                <div class="value">{{ weather.wind }} km/h</div>
            </div>
            <div class="item">
                <div class="label">Precipitation</div>
                <div class="value">{{ weather.rain }} mm</div>
            </div>
        </div>
    </div>
    {% endif %}
</div>
</body>
</html>
"""

def get_weather(city):
    geo = requests.get(
        "https://geocoding-api.open-meteo.com/v1/search",
        params={"name": city, "count": 1, "language": "en"},
        timeout=15
    )
    geo.raise_for_status()
    results = geo.json().get("results", [])

    if not results:
        return None

    place = results[0]

    response = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": place["latitude"],
            "longitude": place["longitude"],
            "current": (
                "temperature_2m,relative_humidity_2m,"
                "apparent_temperature,precipitation,"
                "weather_code,wind_speed_10m"
            ),
            "timezone": "auto"
        },
        timeout=15
    )
    response.raise_for_status()
    current = response.json()["current"]

    conditions = {
        0: "Clear sky", 1: "Mainly clear",
        2: "Partly cloudy", 3: "Overcast",
        45: "Fog", 48: "Fog",
        51: "Light drizzle", 53: "Drizzle",
        55: "Heavy drizzle", 61: "Light rain",
        63: "Moderate rain", 65: "Heavy rain",
        71: "Light snow", 73: "Snow", 75: "Heavy snow",
        80: "Rain showers", 81: "Rain showers",
        82: "Heavy rain showers", 95: "Thunderstorm",
        96: "Thunderstorm with hail",
        99: "Thunderstorm with heavy hail"
    }

    return {
        "city": place["name"] + (
            ", " + place["country"] if place.get("country") else ""
        ),
        "temperature": current["temperature_2m"],
        "feels": current["apparent_temperature"],
        "humidity": current["relative_humidity_2m"],
        "wind": current["wind_speed_10m"],
        "rain": current["precipitation"],
        "condition": conditions.get(
            current["weather_code"], "Conditions unavailable"
        )
    }

@app.route("/", methods=["GET", "POST"])
def home():
    city = ""
    weather = None
    error = None

    if request.method == "POST":
        city = request.form.get("city", "").strip()
        try:
            weather = get_weather(city)
            if weather is None:
                error = "City not found. Check the spelling and try again."
        except requests.RequestException:
            error = "Weather service unavailable. Check your internet connection."

    return render_template_string(
        PAGE, city=city, weather=weather, error=error
    )

if __name__ == "__main__":
    app.run(debug=True)
