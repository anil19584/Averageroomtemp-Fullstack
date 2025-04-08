import os
import psycopg2
from dotenv import load_dotenv
from datetime import datetime, timezone

# Load environment variables
load_dotenv()
url = os.getenv("DATABASE_URL")
connection = psycopg2.connect(url)

# SQL queries
CREATE_ROOMS_TABLE = (
    "CREATE TABLE IF NOT EXISTS rooms (id SERIAL PRIMARY KEY, name TEXT);"
)
CREATE_TEMPS_TABLE = """CREATE TABLE IF NOT EXISTS temperatures (room_id INTEGER, temperature REAL, 
                        date TIMESTAMP, FOREIGN KEY(room_id) REFERENCES rooms(id) ON DELETE CASCADE);"""

INSERT_ROOM_RETURN_ID = "INSERT INTO rooms (name) VALUES (%s) RETURNING id;"
INSERT_TEMP = (
    "INSERT INTO temperatures (room_id, temperature, date) VALUES (%s, %s, %s);"
)

GLOBAL_NUMBER_OF_DAYS = (
    """SELECT COUNT(DISTINCT DATE(date)) AS days FROM temperatures;"""
)
GLOBAL_AVG = """SELECT AVG(temperature) as average FROM temperatures;"""

def create_room(name):
    with connection.cursor() as cursor:
        cursor.execute(CREATE_ROOMS_TABLE)
        cursor.execute(INSERT_ROOM_RETURN_ID, (name,))
        room_id = cursor.fetchone()[0]
        connection.commit()
    return room_id

def insert_temperature(room_id, temperature, date):
    with connection.cursor() as cursor:
        cursor.execute(CREATE_TEMPS_TABLE)
        cursor.execute(INSERT_TEMP, (room_id, temperature, date))
        connection.commit()

def get_global_avg():
    with connection.cursor() as cursor:
        cursor.execute(GLOBAL_AVG)
        average = cursor.fetchone()[0]
        cursor.execute(GLOBAL_NUMBER_OF_DAYS)
        days = cursor.fetchone()[0]
    return average, days