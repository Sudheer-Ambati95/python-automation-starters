# test_weather.py
import os, json

def test_weather_file_exists():
    assert os.path.exists("weather.json")

def test_weather_file_is_valid_json():
    with open("weather.json") as f:
        data = json.load(f)
    assert "main" in data  # OpenWeather has "main" field for temp/humidity
