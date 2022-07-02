class BankAccount:
    def __init__(self, int_rate, balance):
        self.balance = balance
        self.interest = int_rate

    def deposit(self, amount):
		# your code here
        self.balance += amount
        return self

    def withdraw(self, amount):
		# your code here
        if self.balance<amount:
            print("no mas monies")
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
		# your code here
        print(f"Current Balance: ${self.balance} ")

    def yield_interest(self):
		# your code here
        self.balance += self.interest * self.balance
        return self

Checking= BankAccount(0.01, 1000)
Savings = BankAccount(0.01, 5000)

Checking.deposit(50).deposit(50).deposit(50).withdraw(50).yield_interest().display_account_info()
Savings.deposit(100).deposit(100).withdraw(50).withdraw(50).withdraw(50).withdraw(50).yield_interest().display_account_info()