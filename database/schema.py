import os
from dotenv import load_dotenv
import psycopg2

# Load environment variables from .env file
load_dotenv()

database_url = os.getenv('DATABASE_URL')

def create_connection():
    # Use the database URL from the environment variable to establish a connection
    return psycopg2.connect(database_url)

def create_tables():
    commands = ( 
        """
        CREATE TABLE IF NOT EXISTS "User" (
            id UUID PRIMARY KEY,
            email VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL,
            role VARCHAR(50) NOT NULL DEFAULT 'USER',
            person1 VARCHAR(50) NOT NULL DEFAULT 'Person1',
            person2 VARCHAR(50) NOT NULL DEFAULT 'Person2',
            person1Insta VARCHAR(50) NOT NULL DEFAULT '#',
            person2Insta VARCHAR(50) NOT NULL DEFAULT '#',           
            created_at TIMESTAMP DEFAULT NOW(),
            updated_at TIMESTAMP DEFAULT NOW()
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS "Country" (
            id UUID PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            locationId INT NOT NULL,
            visited BOOLEAN DEFAULT TRUE,
            user_id UUID REFERENCES "User"(id),
            created_at TIMESTAMP DEFAULT NOW(),
            updated_at TIMESTAMP DEFAULT NOW()
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS "Event" (
            id UUID PRIMARY KEY,
            type VARCHAR(50) NOT NULL,
            code INT,
            topic VARCHAR(255),
            content TEXT,
            created_by UUID REFERENCES "User"(id),
            created_at TIMESTAMP DEFAULT NOW(),
            updated_at TIMESTAMP DEFAULT NOW()
        )
        """
    )
    conn = None
    try:
        conn = create_connection()
        cur = conn.cursor()
        for command in commands:
            cur.execute(command)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()