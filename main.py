class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def transfer(self, other_account, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            other_account.deposit(amount)
            print(f"Transferred ${amount} to account {other_account.account_number}. New balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid transfer amount.")

class Bank:
    accounts = {}
    current_account = None

    def create_account(self):
        account_number = len(self.accounts) + 1
        balance = float(input("Enter initial deposit amount: "))
        if balance > 0:
            new_account = Account(account_number, balance)
            self.accounts[account_number] = new_account
            print(f"Account created successfully. Account number: {account_number}")
            return new_account
        else:
            print("Initial deposit must be positive.")
            return None

    def select_account(self):
        account_number = int(input("Enter account number: "))
        if account_number in self.accounts:
            self.current_account = self.accounts[account_number]
            print(f"Selected account {account_number}")
        else:
            print("Invalid account number.")

    def deposit(self):
        if self.current_account:
            amount = float(input("Enter deposit amount: "))
            self.current_account.deposit(amount)
        else:
            print("Please select an account first.")

    def withdraw(self):
        if self.current_account:
            amount = float(input("Enter withdrawal amount: "))
            self.current_account.withdraw(amount)
        else:
            print("Please select an account first.")

    def check_balance(self):
        if self.current_account:
            print(f"Account balance: ${self.current_account.balance}")
        else:
            print("Please select an account first.")

    def transfer(self):
        if self.current_account:
            target_account_number = int(input("Enter recipient account number: "))
            if target_account_number in self.accounts:
                amount = float(input("Enter transfer amount: "))
                self.current_account.transfer(self.accounts[target_account_number], amount)
            else:
                print("Invalid recipient account number.")
        else:
            print("Please select an account first.")

def main():
    bank = Bank()
    while True:
        print("\nMenu:")
        print("1. Create new account")
        print("2. Select account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Check balance")
        print("6. Transfer")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            new_account = bank.create_account()
            if new_account:
                print(f"Account number: {new_account.account_number}")
        elif choice == '2':
            bank.select_account()
        elif choice == '3':
            bank.deposit()
        elif choice == '4':
            bank.withdraw()
        elif choice == '5':
            bank.check_balance()
        elif choice == '6':
            bank.transfer()
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
