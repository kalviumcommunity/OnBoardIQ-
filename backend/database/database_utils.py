import pandas as pd
from backend.db_connection import get_connection

def fetch_data(query):
    conn = get_connection()

    if conn is None:
        return None

    try:
        return pd.read_sql_query(query, conn)

    finally:
        conn.close()