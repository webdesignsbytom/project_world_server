import psycopg2

def get_db_connection():
    database_url = "postgres://zllryxch:nw6V9ZVwoBpdd7Zl0QqbmvH9FOX2Mggt@flora.db.elephantsql.com/zllryxch"
    conn = psycopg2.connect(database_url)
    return conn
