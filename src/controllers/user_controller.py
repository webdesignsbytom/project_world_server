import psycopg2
import uuid
from database.database import get_db_connection

def authenticate_user(email, password):
    # Placeholder function to authenticate a user
    # In production, you should check the email and hashed password
    # against your database and return user data if the credentials are valid
    # For now, we'll just return a dummy user if the email is 'test@example.com'
    if email == 'test@example.com' and password == 'password':
        return {'id': 1, 'email': email}
    return None

# Create a new User
def create_new_user(email, password):
    conn = None
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        # 'role' is omitted and will default to 'USER'
        cur.execute('INSERT INTO "User" (id, email, password) VALUES (%s, %s, %s)', (str(uuid.uuid4()), email, password))
        conn.commit()
        return True
    except Exception as e:
        print("An error occurred:", e)
        return False
    finally:
        if conn:
            conn.close()


# Get all users in database
def get_all_users():
    conn = None
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM "User"')
        records = cur.fetchall()
        return records
    except Exception as e:
        print("An error occurred:", e)
        return []
    finally:
        if conn:
            conn.close()