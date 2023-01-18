import sqlite3
import os
from dotenv import load_dotenv
load_dotenv()

DB_URL = os.environ['DATABASE_URL']

def create_connection():
    return sqlite3.connect(DB_URL)

def create_users_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
    conn.commit()
    conn.close()

def insert_users():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.executemany("INSERT INTO users (username, password) VALUES (?, ?)", [("allie", "robinson"), ("jon", "finger"), ("andy", "wong"), ("matthew", "slipper"), ("chad", "chapman"), ("steven", "lu")])
    conn.commit()
    conn.close()

def table_exists(conn, table_name):
    cursor = conn.cursor()
    try:
        cursor.execute(f"SELECT 1 FROM {table_name} LIMIT 1")
    except sqlite3.OperationalError:
        return False
    return True

if __name__ == "__main__":
    breakpoint()