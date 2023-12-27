import os
from dotenv import load_dotenv
import psycopg2
import uuid

# Load environment variables from .env file
load_dotenv()

# Get the database URL from the environment variable
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

def seed_users():
    user_data = [
        (str(uuid.uuid4()), 'user1@example.com', 'password', 'USER'),
        (str(uuid.uuid4()), 'user2@example.com', 'password', 'ADMIN'),
        # Add more users as needed
    ]
    conn = None
    try:
        conn = create_connection()
        cur = conn.cursor()
        cur.executemany("INSERT INTO \"User\"(id, email, password, role) VALUES (%s, %s, %s, %s)", user_data)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def seed_events():
    event_data = [
        (str(uuid.uuid4()), 'ERROR', 'Test event', 500, '500 test content'),
        (str(uuid.uuid4()), 'USER', 'Test event', 200, '200 test content'),
        (str(uuid.uuid4()), 'ADMIN', 'Test event', 201, '201 test content'),
        (str(uuid.uuid4()), 'VISITOR', 'Test event', 201, '201 test content'),
        (str(uuid.uuid4()), 'DEVELOPER', 'Test event', 201, '201 test content')
        # Add more events as needed
    ]
    conn = None
    try:
        conn = create_connection()
        cur = conn.cursor()
        cur.executemany("INSERT INTO \"Event\"(id, type, topic, code, content) VALUES (%s, %s, %s, %s, %s)", event_data)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
  
def create_triggers():
    trigger_functions = (
        """
        CREATE OR REPLACE FUNCTION update_updated_at_column()
        RETURNS TRIGGER AS $$
        BEGIN
            NEW.updated_at = NOW();
            RETURN NEW;
        END;
        $$ language 'plpgsql';
        """,
    )
    triggers = (
        """
        CREATE TRIGGER update_user_updated_at BEFORE UPDATE ON "User"
        FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
        """,
        """
        CREATE TRIGGER update_event_updated_at BEFORE UPDATE ON "Event"
        FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
        """
    )
    conn = None
    try:
        conn = create_connection()
        cur = conn.cursor()
        for function in trigger_functions:
            cur.execute(function)
        for trigger in triggers:
            cur.execute(trigger)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
          
            
def drop_tables():
    commands = (
        """
        DROP TABLE IF EXISTS "Event" CASCADE;
        """,
        """
        DROP TABLE IF EXISTS "User" CASCADE;
        """,
        """
        DROP TABLE IF EXISTS "Country" CASCADE;
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

def main():
    drop_tables()
    create_tables()
    create_triggers()
    seed_users()
    seed_events()


if __name__ == '__main__':
    main()
