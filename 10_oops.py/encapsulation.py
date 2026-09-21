class BankAccount:
    def __init__(self,owner,balance):
        self.owner=owner # public
        self._pin="1234" #  protected
        self.__account_number="123456789" #private
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
print(account._BankAccount__account_number) # way to call private variable
print(account.withdraw(200))
print(account.deposit(500))


class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary
    def get_salary(self):
        return self.__salary
    def set_salary(self,salary):
        self.__salary=salary
    
        
employee=Employee("Alex",50000)
print(employee.get_salary())
employee.set_salary(60000)
print(employee.get_salary())