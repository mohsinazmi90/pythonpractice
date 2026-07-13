class BankAccount:
    def __init__(self, account_number, account_holder, initial_balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₱{amount:,.2f} deposited successfully.")
            self.display_balance()
        else:
            print("Invalid deposit amount. Must be greater than zero.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds! Transaction canceled.")
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            self.balance -= amount
            print(f"₱{amount:,.2f} withdrawn successfully.")
            self.display_balance()

    def display_balance(self):
        print(f"Current Balance for {self.account_holder}: ₱{self.balance:,.2f}")

    def __str__(self):
        return f"Acc No: {self.account_number} | Holder: {self.account_holder} | Balance: ₱{self.balance:,.2f}"


class BankSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, account_holder, initial_deposit):
        if account_number in self.accounts:
            print("Account number already exists!")
        elif initial_deposit < 0:
            print("Initial deposit cannot be negative.")
        else:
            new_account = BankAccount(account_number, account_holder, initial_deposit)
            self.accounts[account_number] = new_account
            print(f"Account successfully created for {account_holder}!")

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)

    def transfer(self, sender_acc_num, receiver_acc_num, amount):
        sender = self.get_account(sender_acc_num)
        receiver = self.get_account(receiver_acc_num)

        if not sender:
            print("Sender account not found.")
            return
        if not receiver:
            print("Receiver account not found.")
            return

        if amount <= 0:
            print("Transfer amount must be positive.")
        elif sender.balance < amount:
            print("Transfer failed. Insufficient funds.")
        else:
            sender.balance -= amount
            receiver.balance += amount
            print(
                f"Successfully transferred ₱{amount:,.2f} from {sender.account_holder} to {receiver.account_holder}."
            )


# --- Interactive Menu System ---
def main():
    bank = BankSystem()

    # Pre-populating a couple of accounts for testing
    bank.create_account("101", "Alice Smith", 5000.0)
    bank.create_account("102", "Bob Jones", 1500.0)
    print("-" * 40)

    while True:
        print("\n=== BANK MANAGEMENT SYSTEM ===")
        print("1. Create New Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transfer Funds")
        print("5. Check Account Details")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()
        print("-" * 40)

        if choice == "1":
            acc_num = input("Enter desired Account Number: ")
            name = input("Enter Account Holder Name: ")
            try:
                deposit = float(input("Enter Initial Deposit: "))
                bank.create_account(acc_num, name, deposit)
            except ValueError:
                print("Invalid input. Please enter numbers for the deposit.")

        elif choice == "2":
            acc_num = input("Enter Account Number: ")
            account = bank.get_account(acc_num)
            if account:
                try:
                    amount = float(input("Enter deposit amount: "))
                    account.deposit(amount)
                except ValueError:
                    print("Invalid input.")
            else:
                print("Account not found.")

        elif choice == "3":
            acc_num = input("Enter Account Number: ")
            account = bank.get_account(acc_num)
            if account:
                try:
                    amount = float(input("Enter withdrawal amount: "))
                    account.withdraw(amount)
                except ValueError:
                    print("Invalid input.")
            else:
                print("Account not found.")

        elif choice == "4":
            sender = input("Enter YOUR Account Number: ")
            receiver = input("Enter RECIPIENT Account Number: ")
            try:
                amount = float(input("Enter amount to transfer: "))
                bank.transfer(sender, receiver, amount)
            except ValueError:
                print("Invalid input.")

        elif choice == "5":
            acc_num = input("Enter Account Number: ")
            account = bank.get_account(acc_num)
            if account:
                print(account)
            else:
                print("Account not found.")

        elif choice == "6":
            print("Thank you for using our banking system. Goodbye!")
            break
        else:
            print("Invalid option. Please choose between 1 and 6.")
        print("-" * 40)


if __name__ == "__main__":
    main()
