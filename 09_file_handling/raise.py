def withdraw(balance,amount):
    if amount>balance:
        raise Exception("Insufficient balance")
    return balance-amount

try:
    withdraw(1000,2000)
except Exception as e:
    print(e)