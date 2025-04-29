class BankAccount:
    def __init__(self, account_name, balance):
        self.account_name = account_name
        self.balance = balance
        self.active = True

    def deposit(self, amount):
        if self.active:
            self.balance += amount
            print(f"Hello {self.account_name}, your deposit was successful. You deposited: {amount}, your current balance is: {self.balance}")
        else:
            print("Your account is deactivated. Please contact support.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Hello {self.account_name}, your withdrawal was successful. You withdrew: {amount}, your current balance is: {self.balance}")
        else:
            print(f"The amount you want to withdraw is not available. Current balance: {self.balance}")

    def deactivate(self):
        if self.balance == 0:
            self.active = False
            print(f"{self.account_name}, your account has been deactivated because the current balance is: {self.balance}")

    def activate(self):
        self.active = True

account1 = BankAccount("Sebastian", 200)
account2 = BankAccount("Tiny", 1000)

account1.deposit(800)
account2.deposit(2000)
account1.withdraw(1000)
account2.withdraw(1000)
