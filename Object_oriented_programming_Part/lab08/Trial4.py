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
class SavingsAccount(Account):
    deposit_charge = 2
    def deposit(self, amount):
        return Account.deposit(self, amount - self.deposit_charge)
class AsSeenOnTVAccount(CheckingAccount, SavingsAccount):
    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 1           # A free dollar!
such_a_deal = AsSeenOnTVAccount("John")
r = such_a_deal.balance

r = such_a_deal.deposit(20)            # $2 fee from SavingsAccount.deposit
print(r)
such_a_deal.withdraw(5)            # $1 fee from CheckingAccount.withdraw

r = [c.__name__ for c in AsSeenOnTVAccount.mro()]
print(r)