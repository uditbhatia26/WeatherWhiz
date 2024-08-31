import requests
import keys


class Weather:
    def __init__(self):
        self.response = requests.get(url=f"https://api.openweathermap.org/data/2.5/forecast", params=keys.weather_parameters)
        self.forecast_value = None
        self.data = self.response.json()
        self.condition_code = None
        self.weather_data = None
        self.will_rain = False
        self.humidity_value = 0
        self.temperature_value = 0

    def check_for_rain(self):
        self.weather_data = self.data["list"][2]
        self.condition_code = self.weather_data["weather"][0]["id"]
        self.forecast_value = self.weather_data["weather"][0]["description"].title()
        self.temperature_value = self.weather_data["main"]["temp"]
        self.humidity_value = self.weather_data["main"]["humidity"]
        if self.condition_code < 600:
            return True
        else:
            return False
