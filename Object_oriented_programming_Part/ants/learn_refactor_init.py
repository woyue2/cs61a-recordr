class Father:
    def __init__(self,money):
        # print(self.money) 未创建先这样会报错
        self.money = money
        print(f"Father has money of {self.money} dollars")
class Son(Father):
    def __init__(self, money):
        super().__init__(money)
        print(f'I just wanna know if it will be different?{money}')
class Sonson(Son):
    def __init__(self, money):
        Son.__init__(self,money)
        print(f'well,it comes to the third layer')
        print('')
        Father.__init__(self,money+1)
        print(f'can it work?')#YES!
        print('PhaseEnd')
"""Call"""
print('1')
Baba = Father(100)
# print("2")
Erzi = Son(10)#这样调用才是正确的
# Erzi = Son.__init__(Erzi,10)# 这样调用是错误的，可以用Class.__init__来改写如lambda self,attr : xx 但是不能call directly
print('3')
Sunzi = Sonson(1)
# print('')

"""method"""
# print(Father.__init__)
# print(Son.__init__)
# print(Sonson.__init__)

# Father.__init__ = lambda self, money: print(">??????")
# Baba = Father(100)

type(Baba)
print("type(Baba)", type(Baba))
print("type(Erzi)", type(Erzi))
print("type(Sunzi)", type(Sunzi))