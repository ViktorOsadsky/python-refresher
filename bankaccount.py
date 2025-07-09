class Bankaccount:
    def __init__(self, balance, name, accountnum):
        self.balance = balance
        self.name = name
        self.accountnum = accountnum

    def withdraw(self, amt):
        self.balance -= amt
        return self.balance

    def deposit(self, amt):
        self.balance += amt
        return self.balance

    def balanceprint(self):
        print(self.balance)
