# real_time_data_processing_py
* This script collects and processes real-time weather data for major metro cities in India.
* It retrieves the current temperature and weather description for each city using the OpenWeatherMap API.
* The script then stores the temperature data and calculates average, maximum, and minimum temperatures.
* It repeatedly updates the data every 5 minutes to ensure continuous tracking of weather trends.
  

Features : 
1) API Call: Fetches weather data for Indian metro cities using OpenWeatherMap.
2) Data Storage: Maintains a record of temperatures for each city (up to the last 10 entries).
3) Aggregates: Calculates average, maximum, and minimum temperatures based on the stored data.
4) Loop: Repeats every 5 minutes to refresh the data for continuous monitoring.
5) Error Handling : Displays error messages if data fetching fails for any city.
   

Requriments : Libraries : Requests , time , collections.

Installation : 
* Clone the repository.
* Install the requried libraries.
* Replace API_KEY in the script with your OpenWeatherMap API Key.
  

Usage : Run the script to start fetching and displaying weather data for the cities.
* Imports : Requests.
            Time.
            Defaultdict.
  
* City Lists : This is a predefined list of major cities in india for which the weather data will be fetched.
  
* API Key : You need an API key from OpenWeatherMap to fectch the weather data.
  
* BASE_URL : The endpoint for fetching weather data.
  
* Weather data store.
  
* Function : get_weather(city).
  1)Sends a GET request to OpenWeatherMap's API to fetch weather data for a specific city.
  
  2)The parameters include the city name, API key, and the unit of temperature (metric for Celsius).
  
  3)Returns the response in JSON format.

* Function : store_weather_data(city,temp).
   1)Stores the temperature temp for a city in the weather_data_store.
  
   2)If there are more than 10 temperature records for a city, it removes the oldest entry to keep only the latest 10.
  

* Function : calculate_aggregates(city)
   1)This function calculates the average, maximum, and minimum temperatures for a city based on its stored data.
  
   2)If there are no temperatures stored for the city, it returns.

* Function : print_weather_data_aggregates(city,weather_data)

* Main Loop : 1)This is the main function that runs an infinite loop.
  
              2) Every 5 minutes (300 seconds), it fetches weather data for all the cities in the cities list and prints the data.
  
              3) After fetching the data, it pauses for 5 minutes before fetching again.

* Entry point : This ensures that the main function is executed only when the script is run directly.

  


