# define the userclass
class Users:
    def __init__(self,user_id,name,phone):
        self.user_id = user_id #initialize user id
        self.name = name  #initialize user name
        self.phone = phone #initialize user phone number
        self.account=Account(self) #creating an account for the user
    def __repr__(self):
        return f'User({self.user_id},{self.name},{self.phone})' #representation of the user
        # object
# define account class
class Account:
    def __init__(self,user):
        self.user = user
        self.balance = 0.0
    def deposit(self,amount):
        if amount > 0: #check if the deposit is more than 0
            self.balance += amount
            print(f"{amount} deposited.New balance: {self.balance}")
        else :
            print("Deposit amount must be positive")
    def withdraw(self,amount):
        if 0 < amount < self.balance: #check if withdrawal amount is valid
            self.balance -= amount
            print(f"{amount} withdrawn.New balance: {self.balance}")
        else :
            print("Insufficient funds or invalid amount")
    def __repr__(self):
        return f'Account( User: {self.user} , Balance: {self.balance})'#representation of
        # account  object
# define the transaction class
class Transaction :
    def __init__(self,account,amount,transaction_type):
        self.account = account
        self.amount = amount
        self.transaction_type = transaction_type
    def process(self):
        if self.transaction_type == "deposit":
            self.account.deposit(self.amount)
        elif self.transaction_type == "withdraw":
            self.account.withdraw(self.amount)
        else:
            print("Invalid transaction type")
    def __repr__(self):
        return f'Transaction(Account:{self.account.user.name},Amount:{self.amount},Type:{self.transaction_type})'

# example usage like an object
user1=Users(1,"Kasudi Charlene", "+254784184065")
print(user1)

#deposit amount
user1.account.deposit(1000)

user1.account.withdraw(500)

transaction1=Transaction(user1.account,200,"deposit")
transaction1.process()

transaction2=Transaction(user1.account,100,"withdraw")
transaction2.process()

print(user1.account)

#another user
user2= Users(2,"Eileen Joy","+254722421532")
print(user2)

user2.account.deposit(5000)

user2.account.withdraw(2500)

transaction1=Transaction(user2.account,2000,"deposit")
transaction1.process()

transaction2=Transaction(user2.account,1500,"withdraw")
transaction2.process()

print(user2.account)

user3=Users(3,"Elias Aguvasu","+254719145302")
print(user3)
user3.account.deposit(1000)
user3.account.withdraw(500)

transaction1=Transaction(user3.account,200,"deposit")
transaction1.process()
transaction2=Transaction(user3.account,1500,"withdraw")
transaction2.process()

print(user3.account)