# Logic to read/write progress data
import sqlite3

def init_db():
    conn = sqlite3.connect('db.sqlite')
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS progress (
            user TEXT,
            topic TEXT,
            problems_solved INTEGER,
            streak INTEGER
        )
    """)
    conn.commit()
    return conn, cursor

def save_progress(user, topic, progress):
    conn, cursor = init_db()
    cursor.execute("INSERT INTO progress (user, topic, problems_solved, streak) VALUES (?, ?, ?, ?)", progress)
    conn.commit()
