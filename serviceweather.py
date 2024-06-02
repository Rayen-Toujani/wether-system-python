import requests

def get_weather(city, api_key):
    base_url = "http://api.weatherapi.com/v1/current.json"
    params = {
        "q": city,
        "key": api_key,

    }
    response = requests.get(base_url, params=params)
    return response.json()

def display_weather(data):
    if "error" in data:
        print("Error:", data["error"]["message"])
        return

    city = data["location"]["name"]
    country = data["location"]["country"]
    weather = data["current"]["condition"]["text"]
    temperature = data["current"]["temp_c"]
    humidity = data["current"]["humidity"]
    wind_speed = data["current"]["wind_kph"]

    print(f"Weather in {city}, {country}:")
    print(f"Description: {weather}")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} kph")


