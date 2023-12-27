# event_controller.py
import psycopg2
from dbclient.database import get_db_connection

def get_all_events():
    conn = None
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM "Event"')  # Adjust the table name if different
        events = cur.fetchall()
        return events
    except Exception as e:
        print("An error occurred:", e)
        return []
    finally:
        if conn:
            conn.close()
