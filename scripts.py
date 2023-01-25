import sqlite3
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

load_dotenv()

DATABASE_URL = os.environ['DATABASE_URL']

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    about = Column(String)
    website = Column(String)
    phone = Column(String)

class Login(Base):
    __tablename__ = "login"
    user_id = Column(Integer, ForeignKey("users.id"))
    email = Column(String, unique=True, index=True)
    password = Column(String)

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