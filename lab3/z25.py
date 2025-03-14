# Napisz klasę BankAccount, która ma atrybut balance i metody deposit(amount) oraz
# withdraw(amount), aktualizujące stan konta.


class BankAccount():
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount
        

b = BankAccount(1000)

b.deposit(100)

print(b.balance)

b.withdraw(200)

print(b.balance)