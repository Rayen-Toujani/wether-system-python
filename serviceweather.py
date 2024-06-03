import requests
import tkinter as tk
from tkinter import messagebox


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

def fetch_and_display_weather():
    city = city_entry.get()
    if not city:
        messagebox.showerror("imput Error", "Please enter a city name")
        return
    weather_data = get_weather(city,api_key)
    if "error"in weather_data:
        messagebox.showerror("APIError", weather_data["error"]["message"])
        return
    displa_weather_in_gui(weather_data)

def displa_weather_in_gui(data):
    city = data["location"]["name"]
    country = data["location"]["country"]
    weather = data["current"]["condition"]["text"]
    temperature = data["current"]["temp_c"]
    humidity = data["current"]["humidity"]
    wind_speed = data["current"]["wind_kph"]

    weather_info = (
        f"Weather in {city}, {country}:\n"
        f"Description: {weather}\n"
        f"Temperature: {temperature}°C\n"
        f"Humidity: {humidity}%\n"
        f"Wind Speed: {wind_speed} kph"
    )
    messagebox.showinfo("Weather Information", weather_info)

api_key = "8fd1186d5f284ed1a12231124240206"

app = tk.Tk()
app.title("Weather App")

tk.Label(app, text="Enter city name:").pack()
city_entry = tk.Entry(app)
city_entry.pack()

tk.Button(app,text="Get Weather",command=fetch_and_display_weather).pack()

app.mainloop()