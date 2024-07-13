# payments.py

from database import conn, cursor
import datetime  # Import the datetime module for date handling

def add_payment(party_name, amount):
    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Use datetime.datetime
    cursor.execute('INSERT INTO payments (party_name, amount, date) VALUES (?, ?, ?)', (party_name, amount, date))
    conn.commit()
    print(f"Payment added for {party_name} of amount {amount}")

def get_payments_for_party(party_name):
    cursor.execute('SELECT * FROM payments WHERE party_name=?', (party_name,))
    return cursor.fetchall()
