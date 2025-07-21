import datetime
import psycopg2

def log_entry(text, mood, url):
    try:
        conn = psycopg2.connect(
            host="mood-ai-466609:asia-south1:mood-detect",
            database="mood",
            user="postgres",
            password="1234"
        )
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS mood_logs (
                id SERIAL PRIMARY KEY,
                text TEXT,
                mood TEXT,
                url TEXT,
                timestamp TIMESTAMP
            )
        """)
        cursor.execute("INSERT INTO mood_logs (text, mood, url, timestamp) VALUES (%s, %s, %s, %s)",
                       (text, mood, url, datetime.datetime.now()))
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print("DB Error:", e)
