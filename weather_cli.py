# weather_cli.py
import requests, argparse, json, sys

parser = argparse.ArgumentParser(description="Fetch weather data")
parser.add_argument("city", help="City name")
args = parser.parse_args()

API_KEY = "your_api_key"  # 🔑 replace with OpenWeather API key
url = f"http://api.openweathermap.org/data/2.5/weather?q={args.city}&appid={API_KEY}&units=metric"

try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    data = response.json()
except requests.RequestException as e:
    print(f"Error fetching weather: {e}", file=sys.stderr)
    sys.exit(1)

with open("weather.json", "w") as f:
    json.dump(data, f, indent=2)

print(f"✅ Weather for {args.city} saved to weather.json")
