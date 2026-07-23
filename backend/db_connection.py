import psycopg2
from backend.config import DB_CONFIG

def get_connection():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        print("PostgreSQL connected")
        return conn

    except Exception as e:
        print("Connection failed")
        print(e)
        return None


if __name__ == "__main__":
    conn = get_connection()

    if conn:
        conn.close()
        print("Connection closed")