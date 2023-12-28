import uuid
from dbclient.database import get_db_connection


# Get all users in database
def get_all_accounts():
    conn = None
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM "Account"')
        records = cur.fetchall()
        return records
    except Exception as e:
        print("An error occurred:", e)
        return []
    finally:
        if conn:
            conn.close()


# Create a new Account
def create_new_account(email, password):
    conn = None
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        # 'role' is omitted and will default to 'USER'
        cur.execute(
            'INSERT INTO "Account" (id, email, password) VALUES (%s, %s, %s)',
            (str(uuid.uuid4()), email, password),
        )
        conn.commit()
        return True
    except Exception as e:
        print("An error occurred:", e)
        return False
    finally:
        if conn:
            conn.close()
            
            
# Create a new Account
def delete_account(account_id):
    conn = None
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('DELETE FROM "Account" WHERE id = %s', (account_id,))
        affected_rows = cur.rowcount  # Get the number of rows affected
        conn.commit()
        return affected_rows > 0  # Return True if an account was deleted
    except Exception as e:
        print("An error occurred:", e)
        return False
    finally:
        if conn:
            conn.close()
