import os
from dotenv import load_dotenv

# Load environment variables from .env file (for local development)
load_dotenv()

# Adjust to use Render environment variable names
DATABASE_HOST = os.getenv('DATABASE_HOST')
DATABASE_PORT = os.getenv('DATABASE_PORT')
DATABASE_NAME = os.getenv('DATABASE_NAME')
DATABASE_USER = os.getenv('DATABASE_USER')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
#DATABASE = os.getenv('POSTGRESQL_DATABASE_URL')


def get_database_url():
    database_url = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
    print(f"Using database URL: {database_url}")  # Log the database URL for verification
    return database_url
