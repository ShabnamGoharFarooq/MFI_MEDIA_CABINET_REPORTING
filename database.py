import sqlite3

DATABASE = 'My_database'
def connect_db():
    conn = sqlite3.connect(DATABASE)
    conn.execute("PRAGMA foreign_keys = 1")  # Enable foreign key constraints
    return conn
# SQLite database connection
