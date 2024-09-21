# WhatsApp Weather Updates Bot 🌦️

This project is a **WhatsApp bot** built using **Python** and the **OpenWeather API** to fetch daily weather updates. The bot sends weather information to a list of WhatsApp contacts through the **UltraMsg API**, ensuring users are prepared for the day's weather before heading out.

## Features

- Fetches weather data from the OpenWeather API.
- Sends automated daily weather updates via WhatsApp using UltraMsg API.
- Customizable to send messages to any number of contacts.
- Easy to configure and run as a daily cron job.

## Tech Stack

- **Python**: Main programming language.
- **OpenWeather API**: For retrieving weather data.
- **UltraMsg API**: For sending WhatsApp messages.

## Installation

### Prerequisites

- **Python 3.x**: Make sure Python is installed. You can download it from [here](https://www.python.org/downloads/).
- **OpenWeather API Key**: Sign up at [OpenWeather](https://openweathermap.org/api) and get your API key.
- **UltraMsg Account**: Sign up at [UltraMsg](https://www.ultramsg.com/) and get your API credentials.

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/uditbhatia26/weather-updates-whatsapp.git
   cd weather-updates-whatsapp
   ```

2. Set up your environment variables or API credentials:
   - Create a `.env` file or directly add your **OpenWeather API key**, **UltraMsg API key**, and **contact numbers** to the script.

3. Configure the script to fetch weather data for your location.

4. Run the bot to send weather updates:

   ```bash
   python main.py
   ```

## Usage

1. The bot fetches the weather data from the **OpenWeather API**.
2. Weather information is formatted and sent to the specified WhatsApp numbers using **UltraMsg API**.
3. You can modify the timing of the weather update by scheduling the script with **cron jobs**.

## Example Output

The bot sends messages like:

```yaml
Good morning! ☀️
Here’s your weather update for today:
Temperature: 25°C
Conditions: Clear sky 🌤️
Humidity: 60%
Wind Speed: 10 km/h 🌬️
Stay prepared before heading to college!
```

## Customization

- You can modify the location for weather updates by changing the **OpenWeather API** query.
- Update the list of WhatsApp numbers in the script to add more recipients.

## Future Enhancements

- Add multiple location support.
- Implement weather alerts for extreme conditions.
