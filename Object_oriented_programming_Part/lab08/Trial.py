# class <name>:
#     <suite>
class Account:
    def __init__(self, account_holder):
        # xx.attribute = data_indeed
        self.balance = 0
        self.holder = account_holder
a = Account('Kirk')
r = a.balance
print(r)#0
r = a.holder
print(r)#Kirk
b = Account('Spock')
b.balance = 200#change_the_default_value
print(b.balance)#200
# 
r = [acc.balance for acc in (a, b)]#原来可以这样组成list
print(r)#[0, 200]

print(a is a)#True
print(a is not b)#True
c = a
print(c.holder,c is a )#Kirk Trues