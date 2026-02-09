import psycopg2
from psycopg2.extras import execute_batch


def load_weather_data(records, db_config):
    """
    Loads transformed weather records into PostgreSQL.
    
    """

    if not records:
        print("No records to load.")
        return

    connection = psycopg2.connect(
        host=db_config["host"],
        database=db_config["database"],
        user=db_config["user"],
        password=db_config["password"]
    )

    cursor = connection.cursor()

    insert_query = """
        INSERT INTO weather_data (
            date,
            max_temperature,
            min_temperature,
            precipitation,
            max_wind_speed
        )
        VALUES (%s, %s, %s, %s,%s)
    """

    data_to_insert = [
        (
            record["date"],
            record["max_temperature"],
            record["min_temperature"],
            record["precipitation_sum"],
            record["max_wind_speed"]
        )
        for record in records
    ]

    execute_batch(cursor, insert_query, data_to_insert)

    connection.commit()
    cursor.close()
    connection.close()

    print(f"Loaded {len(data_to_insert)} daily records into weather_data.")
