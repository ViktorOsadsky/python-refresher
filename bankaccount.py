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


bc = Bankaccount(1000, "Viktor", 100)
bc.withdraw(20)
bc.deposit(30)
bc.balanceprint()
bc.withdraw(200)
bc.deposit(0)
bc.balanceprint()
bc.withdraw(0)
bc.deposit(300000)
bc.balanceprint()
