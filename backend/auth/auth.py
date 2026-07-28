import bcrypt
def hash_password(password):

    hashed = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    )

    return hashed.decode()
def verify_password(password, password_hash):

    return bcrypt.checkpw(
        password.encode(),
        password_hash.encode()
    )