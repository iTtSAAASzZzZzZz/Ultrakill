import sqlite3

conn = sqlite3.connect('database.db')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS orders(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            total_price REAL,
            FOGEIGN KEY (user_id)
            REFERENCES users(id))''')
cur.commit()
conn.close()
