import sqlite3

# Connect to or create an SQLite database file
conn = sqlite3.connect('cache_test.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table to store data (if it doesn't exist)
cursor.execute('''CREATE TABLE IF NOT EXISTS alien
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT,
                   age INTEGER)''')

# Insert data into the table
data_to_insert = [
    ('Grey', 25),
    ('Reptilian', 230),
    ('Nordic', 522)
]

cursor.executemany('INSERT INTO user (name, age) VALUES (?, ?)', data_to_insert)

# Commit the changes (save to the database)
conn.commit()

conn.close()

