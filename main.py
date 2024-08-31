from weather import Weather
from message import SendMessage


weather_obj = Weather()
message_bot = SendMessage()
if weather_obj.check_for_rain():
    message_bot.rain_message()
else:
    message_bot.sun_message()



