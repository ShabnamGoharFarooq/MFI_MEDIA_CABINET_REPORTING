import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the database path from environment variable or default to 'My_database'
DATABASE = os.getenv('SQLITE_DATABASE_URL', '/mnt/data/My_database.db')

def get_database_path():
    return DATABASE
