# main-0.py

import sys
from bank_account import BankAccount

def main():
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <operation> [amount]")
        return

    operation = sys.argv[1].lower()
    amount = float(sys.argv[2]) if len(sys.argv) > 2 else 0

    account = BankAccount()

    if operation == 'deposit':
        account.deposit(amount)
    elif operation == 'withdraw':
        success = account.withdraw(amount)
        if not success:
            print("Withdrawal failed.")
    elif operation == 'balance':
        account.display_balance()
    else:
        print("Invalid operation. Use 'deposit', 'withdraw', or 'balance'.")

if __name__ == "__main__":
    main()

