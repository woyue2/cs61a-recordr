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
a = Account('sb')
print(a.balance,a.holder)#0 sb
r = a.deposit(10)
print(r)#10
r = a.withdraw(1)
print(r)#9
r = a.withdraw(10)
print(r)#Insufficient funds 取不出不会加减运算
r = getattr(a,'balance')
print(r)#9
r = hasattr(a,'balance')
print(r)
r = type(Account.deposit)
print(r)#<class 'function'>
r = type(a.deposit)
print(r)#<class 'method'>
r = Account.deposit(a,100)
print(r)#109
r = a.deposit(100)
print(r)#209