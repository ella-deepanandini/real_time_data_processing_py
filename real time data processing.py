import requests
import time
from collections import defaultdict
# List of major metro cities in India
cities = ["Mumbai", "Delhi", "Bengaluru", "Kolkata", "Chennai", "Hyderabad", "Ahmedabad"]

# Your OpenWeatherMap API key
API_KEY = "0bf8aa3c53304662d7cb95fdfec24ba4"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
weather_data_store = defaultdict(list)

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # For temperature in Celsius
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()
def store_weather_data(city,temp):
    weather_data_store[city].append(temp)
    if len(weather_data_store[city])>10:
        weather_data_store[city].pop(0)
def calculate_aggregates(city):
            temperatures = weather_data_store[city]
            if not temperatures:
                return None
            avg_temp = sum(temperatures) / len(temperatures)
            max_temp = max(temperatures)
            min_temp = min(temperatures)
            return{
                'avg_temp': avg_temp,
                'max_temp': max_temp,
                'min_temp': min_temp
            }

def print_weather_data_aggregates(city,weather_data):
    if weather_data.get("cod") != 200:
        print(f"Error fetching weather data for {city}:{weather_data.get('message')}")
        return
    
    temp = weather_data['main']['temp']
    weather_description = weather_data['weather'][0]['description']
    store_weather_data(city,temp)
    aggregates =calculate_aggregates(city)
    print(f"City: {city}, Temperature: {temp}°C, Weather: {weather_description}")
    if aggregates:
        print(f"city:{city},avg temp:{aggregates['avg_temp']:.2f}c,max temp:{aggregates['max_temp']}c,min temp:{aggregates['min_temp']}c")
        print('-'* 50)
def main():
    while True:
        print(f"Fetching weather data for metro cities in india")
        for city in cities:
            weather_data = get_weather(city)
            print_weather_data_aggregates(city,weather_data)
            
        time.sleep(300)  

if __name__ == "__main__":
    main()