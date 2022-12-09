import requests
import psycopg2

# endpoint for getting radio station information
ENDPOINT = "http://example.com/api/station"

# PostgreSQL database details
DB_NAME = "mydatabase"
DB_USER = "postgres"
DB_PASSWORD = "password"

# function to get radio station information from endpoint
def get_station_info(endpoint):
    response = requests.get(endpoint)
    if response.status_code == 200:
        station_data = response.json()
        return (station_data["station_name"], station_data["station_freq"], station_data["station_state"], station_data["station_uuid"])
    else:
        return None

# function to seed PostgreSQL database with radio station information
def seed_database(station_info):
    # connect to PostgreSQL database
    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD)
    cursor = conn.cursor()

    # insert radio station information into database
    cursor.execute("INSERT INTO radiostation_catalogues (station_name, station_freq, station_state, station_url,station_uuid) VALUES (%s, %s, %s, %s)", station_info)

    # insert streams for radio station into database
    for stream in station_data["streams"]:
        cursor.execute("INSERT INTO radiostation_streams (station_uuid, is_analyzed, audio_uid, audio_name) VALUES (%s, %s, %s, %s, %s)", (station_data["station_uuid"], stream["is_analyzed"], stream["audio_uid"], stream["audio_name"], stream["url"]))

    conn.commit()

    # close database connection
    cursor.close()
    conn.close()

# continuously seed database with radio station information from endpoint
while True:
    station_info = get_station_info(ENDPOINT)
    if station_info:
        seed_database(station_info)
