import os
#from dotenv import load_dotenv

# Load environment variables from .env file (for local development)
#load_dotenv()

# Get the database path from environment variable or default to local file
DATABASE = ('My_database')

def get_database_path():
    print(f"Using database path: {DATABASE}")  # Log the database path for verification
    return DATABASE