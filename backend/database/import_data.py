import pandas as pd
import sys
import os

# Get backend folder path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Allow Python to find db_connection.py
sys.path.append(BASE_DIR)

from db_connection import get_connection

# Full path to departments.csv
csv_path = os.path.join(BASE_DIR, "data", "departments.csv")

# Read CSV
df = pd.read_csv(csv_path)

conn = get_connection()

if conn:
    cursor = conn.cursor()

    for _, row in df.iterrows():
        cursor.execute(
            """
            INSERT INTO departments (dept_id, dept_name)
            VALUES (%s, %s)
            """,
            (
                int(row["dept_id"]),
                row["dept_name"]
            )
        )

    conn.commit()

    print("Departments imported successfully!")

    cursor.close()
    conn.close()