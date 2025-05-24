import sqlite3

conn = sqlite3.connect('database.db')
cur = conn.cursor()

# Створюємо таблицю
cur.execute('''
CREATE TABLE IF NOT EXISTS weapons (
    name TEXT,
    price INTEGER,
    gamage REAL,
    headshot REAL,
    alternategamage REAL,
    alternateheadshot REAL
)
''')

# Додаємо дані
weapons_data = [
    ("Feedbacker", None, 1, 1, None, None),
    ("Knuckleblaster", None, 2.5+1, 2.5+1, None, None),
    ("Whiplash", None, 0.2, 0.2, None, None),

    ("Piercer Revolver", None, 1, 2, 3, 4.5/6),
    ("Marksman Revolver", 7500, 1, 2, 2, 2),
    ("Sharpshooter Revolver", 25000, 1, 2, 3, 6),
    ("Alternate Piercer", None, 2.5, 5, 7.5, 12.5),
    ("Alternate Marksman", None, 2.5, 5, 5.25, 5.25),
    ("Alternate Sharpshooter", None, 2.5, 5, 5, 10),

    ("Core Eject Shotgun", None, 3*(0.25/12), 3*(0.25/10), 3.5, 3.5),
    ("Pump Charge Shotgun", 12500, 2.5*(0.25/10), 2.5*(0.25/10), 4*(0.25/16), 6*(0.25/24)),
    ("Sawed-On Shotgun", 25000, 3*(0.25/12), 3*(0.25/10), 0.25/1.5, 0.25/1.5),
    ("Green Jackhammer", None, 3, 3, None, None),
    ("Yellow Jackhammer", None, 6, 6, None, None),
    ("Red Jackhammer", None, 10, 10, None, None),

    ("Attractor Nailgun", None, 0.205, 0.205, None, None),
    ("Overheat Nailgun", 25000, 2.3125/4.625, 2.3125/4.625, 11.47, 11.47),
    ("Jumpstart Nailgun", 35000, 2.96/4.625, 2.96/4.625, 10, 10),
    ("Sawblade Launcher", None, 0.75/2.25, 0.75/2.25, None, None),
    ("Sawblade Launcher", None, 0.75/2.25, 0.75/2.25, 0.75*50%, 0.75*50%),
    ("Sawblade Launcher", None, 0.75/2.25, 0.75/2.25, None, None),

    ("Electric Railcannon", None, 8, 8, None, None),
    ("Screwdriver Railcannon", 100000, 3/7.25+5, 8, None, None),
    ("Malicious Railcannon", 100000, 2+6.25, 2+6.25, None, None),

    ("Electric Railcannon", None, None/3.5/7, None/3.5/7, None/3.5/7, None/3.5/7),

]

# Вставляємо дані у таблицю
cur.executemany('''
INSERT INTO weapons (name, price, gamage, headshot, alternategamage, alternateheadshot)
VALUES (?, ?, ?, ?, ?, ?)
''', weapons_data)

# Зберігаємо зміни і закриваємо з'єднання
conn.commit()
conn.close()