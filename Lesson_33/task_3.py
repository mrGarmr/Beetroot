# The Weather app

# Write a console application which takes as an input a city name and returns current weather in the format of your choice.
# For the current task, you can choose any weather API or website
# or use openweathermap.org

import requests

API_KEY = "89bc576819bf729d6e4e644417bfdace"
API_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    """Fetches weather data for a given city."""
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",  # Fetch temperature in Celsius
    }

    try:
        response = requests.get(API_URL, params=params)
        response.raise_for_status()  # Raise an error for invalid responses
        weather_data = response.json()

        # Extract necessary details
        city_name = weather_data["name"]
        temp = weather_data["main"]["temp"]
        feels_like = weather_data["main"]["feels_like"]
        humidity = weather_data["main"]["humidity"]
        weather_desc = weather_data["weather"][0]["description"].capitalize()

        # Display weather details
        print("\nWeather Report for", city_name)
        print("Temperature:", temp, "°C")
        print("Feels Like:", feels_like, "°C")
        print("Humidity:", humidity, "%")
        print("Condition:", weather_desc)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
    except KeyError:
        print("City not found! Please check the name and try again.")


# Main loop
if __name__ == "__main__":
    while True:
        city = input("\nEnter city name (or type 'exit' to quit): ").strip()
        if city.lower() == "exit":
            break
        get_weather(city)
