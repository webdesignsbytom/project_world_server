import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_db_connection():
    database_url = os.getenv('DATABASE_URL')
    print(database_url)
    conn = psycopg2.connect(database_url)
    return conn