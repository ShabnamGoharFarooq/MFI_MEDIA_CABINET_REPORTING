import os
from dotenv import load_dotenv

# Load environment variables from .env file (for local development)
load_dotenv()

# Get the database path from environment variable or default based on environment
DATABASE = os.getenv('SQLITE_DATABASE_URL')

if DATABASE is None:
    # Check if running in a deployment environment like Render
    if os.getenv('RENDER_EXTERNAL_HOSTNAME'):
        DATABASE = '/mnt/data/My_database.sqlite'
    else:
        DATABASE = 'My_database.sqlite'

def get_database_path():
    print(f"Using database path: {DATABASE}")  # Log the database path for verification
    return DATABASE
