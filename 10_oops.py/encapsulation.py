class BankAccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self._pin="1234"
        self.__account_number="123456789"
        self.balance=balance
        
    def withdraw(self,amount):
        self.balance-=amount   
        return self.balance      
    def deposit(self,amount):
        self.balance+=amount
        return self.balance
        

account = BankAccount("Alex", 1000)
print(account.owner)  
print(account._pin)
print(account._BankAccount__account_number)
print(account.withdraw(200))
print(account.deposit(500))