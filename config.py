import os
from dotenv import load_dotenv

# Load environment variables from .env file (for local development)
load_dotenv()

# Get the database path from environment variable
DATABASE = os.getenv('POSTGRESQL_DATABASE_URL')

def get_database_url():
    print(f"Using database URL: {DATABASE}")  # Log the database URL for verification
    return DATABASE
