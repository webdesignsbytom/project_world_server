import psycopg2
import uuid
from dbclient.database import get_db_connection

def authenticate_user(email, password):
    # Placeholder function to authenticate a user
    # In production, you should check the email and hashed password
    # against your database and return user data if the credentials are valid
    # For now, we'll just return a dummy user if the email is 'test@example.com'
    if email == 'test@example.com' and password == 'password':
        return {'id': 1, 'email': email}
    return None


# Create a new User
def create_new_user(email, password, accountType='single', person1='Person1', person2='Person2', person1Insta='#', person2Insta='#'):
    conn = None
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        user_id = str(uuid.uuid4())
        cur.execute(
            'INSERT INTO "User" (id, email, password, accountType, person1, person2, person1Insta, person2Insta) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)', 
            (user_id, email, password, accountType, person1, person2, person1Insta, person2Insta)
        )
        conn.commit()
        return user_id
    except Exception as e:
        print("An error occurred:", e)
        return None
    finally:
        if conn:
            conn.close()


# Update user
def update_user(user_id, user_data):
    conn = None
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        # Prepare the SET part of the SQL query dynamically based on user_data
        set_clause = ', '.join([f"{key} = %s" for key in user_data])
        values = list(user_data.values()) + [user_id]

        query = f'UPDATE "User" SET {set_clause} WHERE id = %s'
        cur.execute(query, values)
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