from bankaccount import BankAccount
class User:
    def __init__(self, name, email, interest_rate=0.02, balance=0):
        self.name = name
        self.email = email
        self.account = BankAccount(interest_rate= interest_rate, balance=balance)	# added this line

    def example_method(self):
    	# we can call the BankAccount instance's methods
        self.account.deposit(100)
    	# or access its attributes
        print(self.account.balance)
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
    
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
    
    def display_user_balance(self):
        print(f"User's Balance: {self.account.balance}")

user = User("ghada", "email@gmail.com")
user.example_method()