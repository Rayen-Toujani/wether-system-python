import requests
import tkinter as tk
from tkinter import messagebox, font

def get_weather(city, api_key):
    base_url = "http://api.weatherapi.com/v1/forecast.json"
    unit = "C" if unit_var.get() == "metric" else "F"
    params = {
        "key": api_key,
        "q": city,
        "days": 3
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": {"message": str(e)}}

def fetch_and_display_weather():
    city = city_entry.get()
    if not city:
        messagebox.showerror("Input Error", "Please enter a city name")
        return
    fetch_and_display_weather_with_city(city)
    if city not in search_history:
        search_history.append(city)
    update_search_history_buttons()

def fetch_and_display_weather_with_city(city):
    weather_data = get_weather(city, api_key)
    if "error" in weather_data:
        messagebox.showerror("API Error", weather_data["error"]["message"])
        return
    display_weather_in_gui(weather_data)

def display_weather_in_gui(data):
    city = data["location"]["name"]
    country = data["location"]["country"]
    current = data["current"]
    forecast = data["forecast"]["forecastday"]

    unit = "°C" if unit_var.get() == "metric" else "°F"
    current_weather = (
        f"Current weather in {city}, {country}:\n"
        f"Description: {current['condition']['text']}\n"
        f"Temperature: {current['temp_c'] if unit == '°C' else current['temp_f']}{unit}\n"
        f"Humidity: {current['humidity']}%\n"
        f"Wind Speed: {current['wind_kph']} kph"
    )

    forecast_weather = "\n\nForecast:\n"
    for day in forecast:
        date = day["date"]
        condition = day["day"]["condition"]["text"]
        max_temp = day["day"]["maxtemp_c"] if unit == '°C' else day["day"]["maxtemp_f"]
        min_temp = day["day"]["mintemp_c"] if unit == '°C' else day["day"]["mintemp_f"]
        forecast_weather += (
            f"{date}:\n"
            f"Condition: {condition}\n"
            f"Max Temp: {max_temp}{unit}\n"
            f"Min Temp: {min_temp}{unit}\n\n"
        )

    weather_info = current_weather + forecast_weather
    weather_label.config(text=weather_info)

def update_search_history_buttons():
    for widget in history_buttons_frame.winfo_children():
        widget.destroy()

    for city in search_history:
        button = tk.Button(history_buttons_frame, text=city, font=button_font, bg="#74b9ff", fg="white",
                           command=lambda c=city: fetch_and_display_weather_with_city(c), bd=5, relief=tk.SOLID,
                           padx=20, pady=5)
        button.pack(pady=5)

api_key = "8fd1186d5f284ed1a12231124240206"
search_history = []

# Initialize the Tkinter application
app = tk.Tk()
app.title("Weather App")

# Set the window size
app.geometry("400x600")

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

# Create and place the unit selection
unit_var = tk.StringVar(value="metric")  # Default to Celsius
tk.Label(app, text="Select unit:", font=label_font, bg="#dff9fb", fg="#130f40").pack()
unit_menu = tk.OptionMenu(app, unit_var, "metric", "imperial")
unit_menu.pack(pady=5)

# Create and place the button that fetches and displays the weather
fetch_button = tk.Button(app, text="Get Weather", font=button_font, bg="#74b9ff", fg="white",
                         command=fetch_and_display_weather, bd=0, relief=tk.SOLID, padx=10, pady=5)
fetch_button.pack(pady=10)

# Create and place the label that will display the weather information
weather_label = tk.Label(app, font=label_font, bg="#dff9fb", fg="#130f40", justify=tk.LEFT, wraplength=300)
weather_label.pack(pady=10)

# Create a frame for the history buttons
history_buttons_frame = tk.Frame(app, bg="#dff9fb")
history_buttons_frame.pack(pady=10)

# Run the Tkinter main loop
app.mainloop()


