import sqlite3
import os


DB_PATH = "data/hash_history.db"


def init_db():

    os.makedirs("data", exist_ok=True)

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS hashes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT,
        hash TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_hash(filename, hash_value):

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO hashes(filename, hash) VALUES (?,?)",
        (filename, hash_value)
    )

    conn.commit()
    conn.close()


def get_hash(filename):

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute(
        "SELECT hash FROM hashes WHERE filename=? ORDER BY id DESC LIMIT 1",
        (filename,)
    )

    result = cursor.fetchone()

    conn.close()

    return result[0] if result else None