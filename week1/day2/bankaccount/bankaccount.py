class BankAccount:
    accounts = []
    # don't forget to add some default values for these parameters!
    def __init__(self, interest_rate, balance = 0): 
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
        self.interest_rate = interest_rate
        self.balance = balance
        BankAccount.accounts.append(self)
        
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        # your code here
        if (self.balance - amount) > 0:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        # your code here
        return self

    def yield_interest(self):
        # your code here
        if self.balance > 0:
            self.balance += (self.balance * self.interest_rate)
        return self
    @classmethod
    def printInstance(cls):
        for account in cls.accounts:
            account.display_account_info()
        

first_account = BankAccount(2, 100)
second_account = BankAccount(5, 5000)
first_account.deposit(60).deposit(150).deposit(300).withdraw(1000).yield_interest()
second_account.deposit(5000).deposit(200000).withdraw(3000).withdraw(12000).withdraw(200).withdraw(950).yield_interest().display_account_info()
BankAccount.printInstance()
