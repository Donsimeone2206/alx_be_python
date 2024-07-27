class BankAccount:
    
    def __init__(self, account_balance):
        self.user_account_balance = account_balance

    def deposit(self, amount):
        self.user_account_balance =+ amount

    def withdraw(self, amount):
        amount = float(amount)
        if self.user_account_balance > amount:
            self.user_account_balance =- amount
            return True
        else:
            False
    
    def display_balance(self):
         self.user_account_balance = float(self.user_account_balance)
         print(f"Current Balance: ${self.user_account_balance:.2f}")
