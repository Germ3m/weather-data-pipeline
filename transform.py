from datetime import datetime

def transform_weather_data(raw_data):

    hourly = raw_data.get("hourly", {})
    times = hourly.get("time", [])
    temperature = hourly.get("temperature_2m", [])
    humidity = hourly.get("relative_humidity_2m", [])
    precipitation = hourly.get("precipitation", [])
    wind_speed = hourly.get("wind_speed_10m", [])

    transformed_data = []

    for i in range(len(times)):
        
        record = {
            "timestamp": datetime.fromisocalendar(times[i]),
            "temperature": temperature[i],
            "humidity": humidity[i],
            "wind_speed": wind_speed[i]
        }
        
        print(transformed_data)

        return transformed_data
    

