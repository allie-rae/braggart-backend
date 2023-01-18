from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from scripts import create_connection, table_exists, create_users_table, insert_users

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

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