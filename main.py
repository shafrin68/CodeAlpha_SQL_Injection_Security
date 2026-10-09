import sqlite3
import bcrypt

# Connect to database
conn = sqlite3.connect("secure_users.db")
cursor = conn.cursor()

# Create user table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password_hash BLOB
)
""")

conn.commit()


def register_user(username, password):
    password_hash = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    )

    try:
        cursor.execute(
            "INSERT INTO users (username, password_hash) VALUES (?, ?)",
            (username, password_hash)
        )
        conn.commit()
        print("Registration successful!")

    except sqlite3.IntegrityError:
        print("Username already exists!")


def login_user(username, password):
    cursor.execute(
        "SELECT password_hash FROM users WHERE username = ?",
        (username,)
    )

    result = cursor.fetchone()

    if result and bcrypt.checkpw(
        password.encode("utf-8"),
        result[0]
    ):
        print("Login successful!")
    else:
        print("Invalid username or password!")


# Register sample user
register_user("sathya", "MySecurePassword123")

# Login
username = input("Enter username: ")
password = input("Enter password: ")

login_user(username, password)

conn.close()
