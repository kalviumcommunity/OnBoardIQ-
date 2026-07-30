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
        is_active
    FROM users
    WHERE email = %s;
    """

    cursor.execute(query, (email,))
    user = cursor.fetchone()

    cursor.close()
    conn.close()

    if user is None:
        return None

    if not user[5]:
        return None

    if verify_password(password, user[3]):
        return {
            "user_id": user[0],
            "name": user[1],
            "email": user[2],
            "role": user[4],
            "is_active": user[5]
        }

    return None