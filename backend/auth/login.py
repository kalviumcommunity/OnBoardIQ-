from backend.db_connection import get_connection
from backend.auth.auth import verify_password


def login_user(email, password):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT
        user_id,
        name,
        email,
        password_hash,
        role,
        is_active,
        last_login
    FROM users
    WHERE email = %s;
    """

    cursor.execute(query, (email,))
    user = cursor.fetchone()


    if user is None:
        cursor.close()
        conn.close()
        return None

    if not user[5]:
        cursor.close()
        conn.close()
        return None

    if verify_password(password, user[3]):

        cursor.execute(
            """
            UPDATE users
            SET last_login = CURRENT_TIMESTAMP
            WHERE user_id = %s;
            """,
            (user[0],)
        )

        conn.commit()

        cursor.execute(query, (email,))
        user = cursor.fetchone()

        cursor.close()
        conn.close()

        return {
            "user_id": user[0],
            "name": user[1],
            "email": user[2],
            "role": user[4],
            "is_active": user[5],
            "last_login": user[6]

        }

    cursor.close()
    conn.close()

    return None