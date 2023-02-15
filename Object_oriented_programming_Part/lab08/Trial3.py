class Account:
    def __init__(self, account_holder):
        # xx.attribute = data_indeed
        self.balance = 0
        self.holder = account_holder
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance
    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance
class CheckingAccount(Account):
    """A bank account that charges for withdrawals."""
    withdraw_charge = 1#手续费
    interest = 0.01
    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_charge)#手续费在这里加入了
checking = CheckingAccount('Sam')
r = checking.deposit(10)
print(r)
r = checking.withdraw(5)
print(r)
r = checking.interest
print(r)