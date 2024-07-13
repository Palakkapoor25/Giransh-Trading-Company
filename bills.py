# bills.py

from database import conn, cursor
import datetime  # Import the datetime module for date handling

def add_bill(party_name, amount):
    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Use datetime.datetime
    cursor.execute('INSERT INTO bills (party_name, amount, date) VALUES (?, ?, ?)', (party_name, amount, date))
    conn.commit()
    print(f"Bill added for {party_name} of amount {amount}")

def get_bills_for_party(party_name):
    cursor.execute('SELECT * FROM bills WHERE party_name=?', (party_name,))
    return cursor.fetchall()
