import tkinter as tk
from tkinter import messagebox, simpledialog

class ATMApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM Machine")
        self.root.geometry("800x600")
        self.root.configure(bg='black')

        self.card_inserted = False
        self.pin_entered = False
        self.account_balance = 10000

        self.create_widgets()

    def create_widgets(self):
        # Title
        title = tk.Label(self.root, text="Your Bank ATM", bg='black', fg='white', font=('Arial', 24))
        title.pack(pady=10)

        # Insert Card
        self.card_label = tk.Label(self.root, text="Please insert your card", bg='black', fg='white', font=('Arial', 16))
        self.card_label.pack(pady=10)

        # PIN Entry
        self.pin_frame = tk.Frame(self.root, bg='black')
        self.pin_frame.pack(pady=10)

        self.pin_label = tk.Label(self.pin_frame, text="Enter your PIN:", bg='black', fg='white', font=('Arial', 16))
        self.pin_label.pack(side='left', padx=5)

        self.pin_entry = tk.Entry(self.pin_frame, show='*', font=('Arial', 16), width=10)
        self.pin_entry.pack(side='left', padx=5)

        self.submit_button = tk.Button(self.pin_frame, text="OK", command=self.check_pin, bg='green', fg='white', font=('Arial', 14))
        self.submit_button.pack(side='left', padx=5)

        # Options Frame
        self.options_frame = tk.Frame(self.root, bg='black')
        self.options_frame.pack(pady=20)

        self.create_options()

        # Footer
        footer = tk.Label(self.root, text="For assistance, please contact customer service.\n© 2023 Your Bank Name", bg='black', fg='white', font=('Arial', 10))
        footer.pack(side='bottom', pady=10)

    def create_options(self):
        options = [
            "Deposit",
            "Withdraw",
            "Transfer",
            "Account Details",
            "Mini Statement",
            "Regular Payment",
            "Account Balance Details",
            "Select Language Mode",
            "Receipt of Withdraw Money",
            "Transaction Successful",
            "Forgot Password",
            "OTP Verification"
        ]

        for option in options:
            button = tk.Button(self.options_frame, text=option, command=lambda opt=option: self.option_selected(opt), bg='blue', fg='white', font=('Arial', 12))
            button.pack(pady=5, fill='x')

    def check_pin(self):
        if not self.card_inserted:
            self.card_inserted = True
            self.card_label.config(text="Card Inserted. Enter your PIN:")
            self.pin_entry.delete(0, tk.END)
        else:
            pin = self.pin_entry.get()
            if pin == "1234":  # Example PIN
                self.pin_entered = True
                messagebox.showinfo("Success", "PIN accepted. You can now select an option.")
                self.pin_entry.config(state='disabled')
            else:
                messagebox.showerror("Error", "Incorrect PIN. Please try again.")

    def option_selected(self, option):
        if not self.pin_entered:
            messagebox.showwarning("Warning", "Please enter your PIN first.")
            return

        # Handle each option
        if option == "Deposit":
            self.deposit()
        elif option == "Withdraw":
            self.withdraw()
        elif option == "Transfer":
            self.transfer()
        elif option == "Account Details":
            self.account_details()
        elif option == "Mini Statement":
            self.mini_statement()
        elif option == "Regular Payment":
            self.regular_payment()
        elif option == "Account Balance Details":
            self.account_balance_details()
        elif option == "Select Language Mode":
            self.select_language_mode()
        elif option == "Receipt of Withdraw Money":
            self.receipt_of_withdraw_money()
        elif option == "Transaction Successful":
            self.transaction_successful()
        elif option == "Forgot Password":
            self.forgot_password()
        elif option == "OTP Verification":
            self.otp_verification()

    def deposit(self):
        amount = simpledialog.askfloat("Deposit", "Enter the amount to deposit:")
        if amount:
            self.account_balance += amount
            messagebox.showinfo("Deposit", f"Deposit successful. New balance: {self.account_balance}")

    def withdraw(self):
        amount = simpledialog.askfloat("Withdraw", "Enter the amount to withdraw:")
        if amount:
            if amount > self.account_balance:
                messagebox.showerror("Error", "Insufficient balance.")
            else:
                self.account_balance -= amount
                messagebox.showinfo(" ```python#")
                messagebox.showinfo("Withdraw", f"Withdrawal successful. New balance: {self.account_balance}")

    def transfer(self):
        amount = simpledialog.askfloat("Transfer", "Enter the amount to transfer:")
        if amount:
            if amount > self.account_balance:
                messagebox.showerror("Error", "Insufficient balance.")
            else:
                account_number = simpledialog.askstring("Transfer", "Enter the recipient's account number:")
                if account_number:
                    self.account_balance -= amount
                    messagebox.showinfo("Transfer", f"Transfer successful. New balance: {self.account_balance}")

    def account_details(self):
        account_number = self.account_number  # assuming you have an attribute for account number
        account_holder = self.account_holder  # assuming you have an attribute for account holder
        account_type = self.account_type  # assuming you have an attribute for account type

        details = f"Account Number: {account_number}\nAccount Holder: {account_holder}\nAccount Type: {account_type}"
        messagebox.showinfo("Account Details", details)

    def mini_statement(self):
        messagebox.showinfo("Mini Statement", "Transaction 1: Deposit of Rs1000\nTransaction 2: Withdrawal of Rs500\nTransaction 3: Transfer of Rs200")

    def regular_payment(self):
        amount = simpledialog.askfloat("Regular Payment", "Enter the amount to pay:")
        if amount:
            if amount > self.account_balance:
                messagebox.showerror("Error", "Insufficient balance.")
            else:
                self.account_balance -= amount
                messagebox.showinfo("Regular Payment", f"Payment successful. New balance: {self.account_balance}")

    def account_balance_details(self):
        messagebox.showinfo("Account Balance Details", f"Current Balance: {self.account_balance}")

    def select_language_mode(self):
        language = simpledialog.askstring("Select Language Mode", "Enter the language code (e.g. en, es, fr, hindi,marathi):")
        if language:
            messagebox.showinfo("Select Language Mode", f"Language set to {language}")

    def receipt_of_withdraw_money(self):
        amount = simpledialog.askfloat("Receipt of Withdraw Money", "Enter the amount to withdraw:")
        if amount:
            if amount > self.account_balance:
                messagebox.showerror("Error", "Insufficient balance.")
            else:
                self.account_balance -= amount
                messagebox.showinfo("Receipt of Withdraw Money", f"Withdrawal successful. New balance: {self.account_balance}")

    def transaction_successful(self):
        messagebox.showinfo("Transaction Successful", "Transaction successful.")

    def forgot_password(self):
        mobile_number = simpledialog.askstring("Forgot Password", "Enter your registered mobile number:")
        if mobile_number:
            messagebox.showinfo("Forgot Password", "An OTP has been sent to your mobile number.")

    def otp_verification(self):
        otp = simpledialog.askstring("OTP Verification", "Enter the OTP sent to your mobile number:")
        if otp:
            # Here you would normally verify the OTP
            messagebox.showinfo("OTP Verification", "OTP verified successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = ATMApp(root)
    root.mainloop()