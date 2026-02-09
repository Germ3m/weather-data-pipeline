from datetime import datetime

def transform_weather_data(raw_data):

    daily = raw_data.get("daily", {})

    if not daily:
        return []
    
    dates = daily.get("time", [])
    max_temps = daily.get("temperature_2m_max", [])
    min_temps = daily.get("temperature_2m_min", [])
    precipitation = daily.get("precipitation_sum", [])
    max_wind_speed = daily.get("wind_speed_10m_max", [])
    transformed_data = []
    print(precipitation)

    for i in range(len(dates)):
        
        record = {
            "date": dates[i],
            "max_temperature": max_temps[i],
            "min_temperature":min_temps[i],
            "precipitation_sum": precipitation[i],
            "max_wind_speed": max_wind_speed[i]
        }
        
        transformed_data.append(record)

    return transformed_data

    


    

