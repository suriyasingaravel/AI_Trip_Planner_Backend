import os, requests
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city: str) -> str:
    url = (
        "http://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )
    r = requests.get(url, timeout=8)
    if r.status_code != 200:
        return "Real-time weather unavailable."
    data = r.json()
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]
    return f"{temp}°C, {desc}"
