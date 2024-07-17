import psycopg2
from psycopg2.extras import DictCursor
from config import get_database_url

def connect_db():
    database_url = get_database_url()
    print(f"Using database at: {database_url}")  # Log the database URL for verification
    conn = psycopg2.connect(database_url, cursor_factory=DictCursor)
    return conn
