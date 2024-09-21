# WhatsApp Weather Updates Bot 🌦️

This project is a **WhatsApp bot** built using **Python** and **BeautifulSoup** to fetch daily weather updates from the **OpenWeather** website. The bot sends weather information to a list of WhatsApp contacts through the **UltraMsg API**, ensuring users are prepared for the day's weather before heading out.

## Features

- Scrapes weather data from the OpenWeather website.
- Sends automated daily weather updates via WhatsApp using UltraMsg API.
- Customizable to send messages to any number of contacts.
- Easy to configure and run as a daily cron job.

## Tech Stack

- **Python**: Main programming language.
- **BeautifulSoup**: For web scraping weather data from the OpenWeather website.
- **UltraMsg API**: For sending WhatsApp messages.

## Installation

### Prerequisites

- **Python 3.x**: Make sure Python is installed. You can download it from [here](https://www.python.org/downloads/).
- **BeautifulSoup**: Install using pip:

  ```bash
  pip install beautifulsoup4

Here’s the corrected version with proper markdown formatting:

```markdown
## Steps

### Clone the repository:

```bash
git clone https://github.com/yourusername/weather-whatsapp-bot.git
cd weather-whatsapp-bot
```

### Install required Python packages:

```bash
pip install -r requirements.txt
```

### Set up your environment variables or API credentials:

- Create a `.env` file or directly add your **UltraMsg API key** and **contact numbers** to the script.

### Configure the script to scrape weather data for your location.

### Run the bot to send weather updates:

```bash
python weather_bot.py
```

## Usage

1. The bot scrapes the weather data from the OpenWeather website using **BeautifulSoup**.
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

- You can modify the location for weather updates by changing the scraping logic in the script.
- Update the list of WhatsApp numbers in the script to add more recipients.

## Future Enhancements

- Add multiple location support.
- Integrate OpenWeather's API for more detailed weather forecasts.
- Implement weather alerts for extreme conditions.
