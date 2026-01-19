import requests
import json


def extract_weather_data():

    """
    Extract weather data from the Open-Meteo API.
    Returns the full raw json response
    """

    url = "https://api.open-meteo.com/v1/forecast"

    parameter = {
        "latitude": -26.2041,
        "longitude": 28.0473,
        "hourly": [
            "temperature_2m",
            "relative_humidity_2m",
            "precipitation",
            "wind_speed_10m"
        ],
        "timezone": "Africa/Johannesburg"
    }

    response  = requests.get(url, params=parameter)
    response.raise_for_status() 

    return response.json()


def save_data(response: dict):

    """
    Save the weather data to a JSON file.
    """

    with open("weather_data.json", "w") as file:
        json.dump(response, file, indent=2)

        print("Weather data saved to weather_data.json")


if __name__ == "__main__":

    raw_weather_data = extract_weather_data()
    save_data(raw_weather_data)

    print(json.dumps(raw_weather_data, indent=2))  