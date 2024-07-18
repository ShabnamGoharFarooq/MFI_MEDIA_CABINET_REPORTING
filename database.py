import sqlite3
from config import get_database_path

def connect_db():
    database_path = get_database_path()
    print(f"Using database at: {database_path}")  # Log the database path for verification
    conn = sqlite3.connect(database_path)
    conn.execute("PRAGMA foreign_keys = 1")  # Enable foreign key constraints
    return conn
