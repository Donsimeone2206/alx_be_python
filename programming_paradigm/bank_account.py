# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the BankAccount with an optional initial balance."""
        self._account_balance = initial_balance

    def deposit(self, amount):
        """Deposit the specified amount into the account balance."""
        if amount > 0:
            self._account_balance += amount
            print(f"Deposited: ${amount:.1f}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        """Withdraw the specified amount from the account balance if sufficient funds are available."""
        if 0 < amount <= self._account_balance:
            self._account_balance -= amount
            print(f"Withdrew: ${amount:.1f}")
            return True
        else:
            print("Insufficient funds.")
            return False

    def display_balance(self):
        """Display the current account balance."""
        print(f"Current Balance: ${self._account_balance:.2f}")


