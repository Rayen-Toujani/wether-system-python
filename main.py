import serviceweather

def main():
    api_key = "8fd1186d5f284ed1a12231124240206"
    city = input("Enter city name: ")
    weather_data = serviceweather.get_weather(city,api_key)
    serviceweather.display_weather(weather_data)

if __name__ == "__main__":
        main()
