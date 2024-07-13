# main.py

from bills import add_bill, get_bills_for_party
from payments import add_payment, get_payments_for_party

def main_menu():
    print("Welcome to Goransh Trading Company")
    while True:
        print("\nPlease select an option:")
        print("1. Add a bill")
        print("2. Add a payment")
        print("3. View bills for a party")
        print("4. View payments for a party")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            party_name = input("Enter party name: ")
            amount = float(input("Enter bill amount: "))
            add_bill(party_name, amount)
        elif choice == '2':
            party_name = input("Enter party name: ")
            amount = float(input("Enter payment amount: "))
            add_payment(party_name, amount)
        elif choice == '3':
            party_name = input("Enter party name: ")
            bills = get_bills_for_party(party_name)
            if bills:
                print(f"Bills for {party_name}:")
                for bill in bills:
                    print(f"ID: {bill[0]}, Amount: {bill[2]}, Date: {bill[3]}")
            else:
                print(f"No bills found for {party_name}")
        elif choice == '4':
            party_name = input("Enter party name: ")
            payments = get_payments_for_party(party_name)
            if payments:
                print(f"Payments for {party_name}:")
                for payment in payments:
                    print(f"ID: {payment[0]}, Amount: {payment[2]}, Date: {payment[3]}")
            else:
                print(f"No payments found for {party_name}")
        elif choice == '5':
            print("Exiting Goransh Trading Company application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == '__main__':
    main_menu()
