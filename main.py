from fastapi import FastAPI
import sqlite3
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

DATABASE_URL = "test.db"

def create_connection():
    return sqlite3.connect(DATABASE_URL)

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

@app.on_event("startup")
def startup():
    conn = create_connection()
    doesTableExist = table_exists(conn, "users")
    if not doesTableExist:
        create_users_table()
        insert_users()
    conn.close()

@app.get("/users")
def read_users():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM users''')
    rows = cursor.fetchall()
    conn.close()
    return rows

@app.get("/")
def home():
    return {"message": "hello world"}

@app.get("/hello")
def hello(name):
    return {"message": "hello " + name}