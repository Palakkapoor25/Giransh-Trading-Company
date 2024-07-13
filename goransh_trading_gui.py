import tkinter as tk
from tkinter import messagebox
from bills import add_bill, get_bills_for_party
from payments import add_payment, get_payments_for_party

class GoranshTradingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Goransh Trading Company")
        self.create_widgets()

    def create_widgets(self):
        # Frame for adding bills
        frame_add_bill = tk.LabelFrame(self.root, text="Add Bill")
        frame_add_bill.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        tk.Label(frame_add_bill, text="Party Name:").grid(row=0, column=0, padx=5, pady=5)
        self.party_name_bill_entry = tk.Entry(frame_add_bill)
        self.party_name_bill_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_add_bill, text="Amount:").grid(row=1, column=0, padx=5, pady=5)
        self.amount_bill_entry = tk.Entry(frame_add_bill)
        self.amount_bill_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Button(frame_add_bill, text="Add Bill", command=self.add_bill).grid(row=2, columnspan=2, padx=5, pady=10)

        # Frame for adding payments
        frame_add_payment = tk.LabelFrame(self.root, text="Add Payment")
        frame_add_payment.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        tk.Label(frame_add_payment, text="Party Name:").grid(row=0, column=0, padx=5, pady=5)
        self.party_name_payment_entry = tk.Entry(frame_add_payment)
        self.party_name_payment_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_add_payment, text="Amount:").grid(row=1, column=0, padx=5, pady=5)
        self.amount_payment_entry = tk.Entry(frame_add_payment)
        self.amount_payment_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Button(frame_add_payment, text="Add Payment", command=self.add_payment).grid(row=2, columnspan=2, padx=5, pady=10)

        # Frame for viewing bills
        frame_view_bills = tk.LabelFrame(self.root, text="View Bills")
        frame_view_bills.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        tk.Label(frame_view_bills, text="Party Name:").grid(row=0, column=0, padx=5, pady=5)
        self.party_name_view_bills_entry = tk.Entry(frame_view_bills)
        self.party_name_view_bills_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Button(frame_view_bills, text="View Bills", command=self.view_bills).grid(row=0, column=2, padx=5, pady=10)

        self.bills_text = tk.Text(frame_view_bills, height=10, width=50)
        self.bills_text.grid(row=1, columnspan=3, padx=5, pady=5)

        # Frame for viewing payments
        frame_view_payments = tk.LabelFrame(self.root, text="View Payments")
        frame_view_payments.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        tk.Label(frame_view_payments, text="Party Name:").grid(row=0, column=0, padx=5, pady=5)
        self.party_name_view_payments_entry = tk.Entry(frame_view_payments)
        self.party_name_view_payments_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Button(frame_view_payments, text="View Payments", command=self.view_payments).grid(row=0, column=2, padx=5, pady=10)

        self.payments_text = tk.Text(frame_view_payments, height=10, width=50)
        self.payments_text.grid(row=1, columnspan=3, padx=5, pady=5)

    def add_bill(self):
        party_name = self.party_name_bill_entry.get()
        amount = float(self.amount_bill_entry.get())
        add_bill(party_name, amount)
        messagebox.showinfo("Success", f"Bill added for {party_name} of amount {amount}")

    def add_payment(self):
        party_name = self.party_name_payment_entry.get()
        amount = float(self.amount_payment_entry.get())
        add_payment(party_name, amount)
        messagebox.showinfo("Success", f"Payment added for {party_name} of amount {amount}")

    def view_bills(self):
        party_name = self.party_name_view_bills_entry.get()
        bills = get_bills_for_party(party_name)
        self.bills_text.delete(1.0, tk.END)
        if bills:
            for bill in bills:
                self.bills_text.insert(tk.END, f"ID: {bill[0]}, Amount: {bill[2]}, Date: {bill[3]}\n")
        else:
            self.bills_text.insert(tk.END, f"No bills found for {party_name}\n")

    def view_payments(self):
        party_name = self.party_name_view_payments_entry.get()
        payments = get_payments_for_party(party_name)
        self.payments_text.delete(1.0, tk.END)
        if payments:
            for payment in payments:
                self.payments_text.insert(tk.END, f"ID: {payment[0]}, Amount: {payment[2]}, Date: {payment[3]}\n")
        else:
            self.payments_text.insert(tk.END, f"No payments found for {party_name}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = GoranshTradingApp(root)
    root.mainloop()
