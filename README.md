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
