import os

open_weather_api_key = "46f061cd770e6e275844ab5d868cbdb6"

users = {
    "me": "+919717228929",
    "Sid": "+919625061809",
    "Disha": "+919625452082",
    "Harddik": "+919873906760",
    "Arav": "+918448811705",
    "Dad": "+919818067101",
    "Addy": "+918287722378",
    "Aarushi": "+919811259197",
    "Amogh": "+918810656864",
    "Aakash": "+918929676776"
    }

mobile_numbers = list(users.values())
url = "https://api.ultramsg.com/instance91965/messages/chat"
token = "tvgmhudj6efwn3aw"
weather_parameters = {
    "lon": 77.07,
    "lat": 28.64,
    "appid": {open_weather_api_key},
    "cnt": 4,
    "units": "metric",
}
