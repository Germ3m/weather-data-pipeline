from extract import extract_weather_data
from transform import transform_weather_data
from load import load_weather_data

db_config = {
    "host": "localhost",
    "database": "weather_db",
    "user": "postgres",
    "password": "20021980"
}

raw_data = extract_weather_data()
clean_data = transform_weather_data(raw_data)
load_weather_data(clean_data, db_config)
