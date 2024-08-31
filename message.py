import requests
import keys
from weather import Weather


class SendMessage:
    def __init__(self):
        self.weather = Weather()
        self.weather.check_for_rain()

    def rain_message(self):
        for i in range(len(keys.mobile_numbers)):
            message = (f"*Good Morning JI*\n"
                       f"*It may rain today, Bring an Umbrella ☂️*\n\n"
                       f"Description: {self.weather.forecast_value}\n"
                       f"Temperature: {self.weather.temperature_value}°C\n"
                       f"Humidity: {self.weather.humidity_value}")
            payload = f"token={keys.token}&to={keys.mobile_numbers[i]}&body={message}"
            headers = {'content-type': 'application/x-www-form-urlencoded'}
            payload = payload.encode('utf8')
            response = requests.request("POST", keys.url, data=payload, headers=headers)

    def sun_message(self):
        for i in range(len(keys.mobile_numbers)):
            message = (f"*Good Morning JI*\n"
                       f"*It's less likely to rain today*\n\n"
                       f"Description: {self.weather.forecast_value}\n"
                       f"Temperature: {self.weather.temperature_value}°C\n"
                       f"Humidity: {self.weather.humidity_value}")
            payload = f"token={keys.token}&to={keys.mobile_numbers[i]}&body={message}"
            headers = {'content-type': 'application/x-www-form-urlencoded'}
            payload = payload.encode('utf8')
            response = requests.request("POST", keys.url, data=payload, headers=headers)
