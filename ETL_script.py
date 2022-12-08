import requests
import psycopg2

# endpoint for getting user information
ENDPOINT = "http://example.com/api/user"

# PostgreSQL database details
DB_NAME = "mydatabase"
DB_USER = "postgres"
DB_PASSWORD = "password"

# function to get user information from endpoint
def get_user_info(endpoint):
    response = requests.get(endpoint)
    if response.status_code == 200:
        user_data = response.json()
        return (user_data["name"], user_data["age"], user_data["gender"])
    else:
        return None

# function to seed PostgreSQL database with user information
def seed_database(user_info):
    # connect to PostgreSQL database
    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD)
    cursor = conn.cursor()

    # insert user information into database
    cursor.execute("INSERT INTO radiostation_catalogues (station_name, station_freq, station_state, station_uuid) VALUES (%s, %s, %s, %s) RETURNING id", user_info)
    catalogue_id = cursor.fetchone()[0]

    # insert streams for user into database
    for stream in user_data["streams"]:
        cursor.execute("INSERT INTO radiostation_streams (catalogue_id, url) VALUES (%s, %s)", (catalogue_id, stream["url"]))

    conn.commit()

    # close database connection
    cursor.close()
    conn.close()

# continuously seed database with user information from endpoint
while True:
    user_info = get_user_info(ENDPOINT)
    if user_info:
        seed_database(user_info)
