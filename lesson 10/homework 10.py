import sqlite3
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time

DATABASE_NAME = 'weather_data.db'
CITY_WEATHER_URL = 'https://www.weather.com/weather/today/l/CYXX0004'
UPDATE_INTERVAL = 1800

def create_database():
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS weather
                 (date TEXT, time TEXT, temperature REAL)''')
    conn.commit()
    conn.close()

def get_temperature():
    response = requests.get(CITY_WEATHER_URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    temperature_tag = soup.find('span', class_='CurrentConditions--tempValue--3KcTQ')
    temperature = temperature_tag.text.strip().replace('°', '') if temperature_tag else None
    return float(temperature) if temperature else None

def insert_weather_data(temperature):
    now = datetime.now()
    date = now.strftime('%Y-%m-%d')
    time = now.strftime('%H:%M:%S')

    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO weather (date, time, temperature) VALUES (?, ?, ?)", (date, time, temperature))
    conn.commit()
    conn.close()

def update_weather_data():
    try:
        while True:
            temperature = get_temperature()
            if temperature is not None:
                insert_weather_data(temperature)
                print(f'Inserted data: {datetime.now()} - {temperature}°C')
            else:
                print('Failed to retrieve temperature data.')
            time.sleep(UPDATE_INTERVAL)
    except KeyboardInterrupt:
        print("Weather data update stopped by user.")

if __name__ == "__main__":
    create_database()
    update_weather_data()