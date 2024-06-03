import requests
import tkinter as tk
from tkinter import messagebox ,font


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

# Set the window size
app.geometry("400x400")

# Set the background color
app.configure(bg="#dff9fb")

# Define custom fonts
title_font = font.Font(family="Helvetica", size=16, weight="bold")
label_font = font.Font(family="Helvetica", size=12)
button_font = font.Font(family="Helvetica", size=12, weight="bold")

# Create and place the title label
title_label = tk.Label(app, text="Weather App", font=title_font, bg="#dff9fb", fg="#130f40")
title_label.pack(pady=10)

# Create and place the label for city entry
city_label = tk.Label(app, text="Enter city name:", font=label_font, bg="#dff9fb", fg="#130f40")
city_label.pack()

# Create and place the entry for city name
city_entry = tk.Entry(app, font=label_font, width=30, bd=2, relief=tk.SOLID)
city_entry.pack(pady=5)

# Create and place the button that fetches and displays the weather
fetch_button = tk.Button(app, text="Get Weather", font=button_font, bg="#74b9ff", fg="white", command=fetch_and_display_weather, bd=0, relief=tk.SOLID, padx=10, pady=5)
fetch_button.pack(pady=10)

# Create and place the label that will display the weather information
weather_label = tk.Label(app, font=label_font, bg="#dff9fb", fg="#130f40", justify=tk.LEFT, wraplength=300)
weather_label.pack(pady=10)

app.mainloop()