# Program 2: Simple Banking System

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount, "New Balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount, "New Balance:", self.balance)
        else:
            print("Insufficient funds!")

# Example
acc = BankAccount("Bob", 1000)
acc.deposit(500)
acc.withdraw(200)
