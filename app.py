from extract import *
from transform import *

raw_data = extract_weather_data()
clean_data = transform_weather_data(raw_data)

print(clean_data[:4])