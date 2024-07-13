import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('goransh_trading.db')
cursor = conn.cursor()

# Create tables for bills and payments if they don't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS bills (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        party_name TEXT NOT NULL,
        amount REAL NOT NULL,
        date TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS payments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        party_name TEXT NOT NULL,
        amount REAL NOT NULL,
        date TEXT NOT NULL
    )
''')

conn.commit()

# Close the connection
conn.close()

print("Database 'goransh_trading.db' created successfully.")
