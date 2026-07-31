from backend.db_connection import get_connection
from backend.auth.auth import hash_password


def register_user(name, email, password):

    conn = get_connection()
    cursor = conn.cursor()

    # Check if email already exists
    cursor.execute(
        """
        SELECT user_id
        FROM users
        WHERE email=%s;
        """,
        (email,)
    )

    if cursor.fetchone():

        cursor.close()
        conn.close()

        return False, "Email already exists."

    hashed_password = hash_password(password)

    cursor.execute(
        """
        INSERT INTO users
        (
            name,
            email,
            password_hash,
            role,
            is_active
        )
        VALUES
        (
            %s,
            %s,
            %s,
            %s,
            %s
        );
        """,
        (
            name,
            email,
            hashed_password,
            "Employee",
            True
        )
    )

    conn.commit()

    cursor.close()
    conn.close()

    return True, "Account created successfully."