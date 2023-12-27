import psycopg2
from database.database import get_db_connection

def create_new_user(email, username):
    conn = None
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO "prisma"."User" (email, username) VALUES (%s, %s)', (email, username))
        conn.commit()
        return True
    except Exception as e:
        print("An error occurred:", e)
        return False
    finally:
        if conn:
            conn.close()


def get_all_users():
    conn = None
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT email FROM "prisma"."User"')
        records = cur.fetchall()
        return records
    except Exception as e:
        print("An error occurred:", e)
        return []
    finally:
        if conn:
            conn.close()