# image_controller.py
import psycopg2
import uuid
from dbclient.database import get_db_connection

def save_image_metadata(user_id, image_path):
    conn = None
    try:
        conn = get_db_connection()  # Ensure you have this function defined or import it
        cur = conn.cursor()
        cur.execute('INSERT INTO "Image" (id, user_id, image_path) VALUES (%s, %s, %s)', (str(uuid.uuid4()), user_id, image_path))
        conn.commit()
        return True
    except Exception as e:
        print("An error occurred:", e)
        return False
    finally:
        if conn:
            conn.close()
