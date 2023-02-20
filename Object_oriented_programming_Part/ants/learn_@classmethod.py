class Human():
    def __init__(self,whatattr,other):
        self.attr = whatattr
        self.other = other
    def __repr__(self):
        return f'e!{self.attr,self.other}，{(self.attr,self.other) is tuple}'
    @classmethod
    def nvren(cls):
        return cls(['?'],2)
    @classmethod
    def renyao(cls):
        return cls(555,666),cls(111,222)
    @staticmethod
    def wusuowei(a):
        return a 
nanRen = Human("jibada",2)
print(nanRen)#有repr才有输出，否则就是输出function,输出什么看repr选了什么attribute;非tuple，不过会用()括起来
print(nanRen.__dict__)#输出为dictionary，包括所有属性，与repr无关
nanRen = Human(1,2)
print(nanRen)
print(nanRen.__dict__)
"""classmethod就是封装好参数，语义化更强，可读性强"""
nvRen = Human.nvren()
print(nvRen)
renYao = Human.renyao()#classmethod的意义在于封装参数，sematic更好，
print(renYao)
renYao2 = Human(555,666)#还是需要输入参数
print(renYao2)
print(renYao is renYao2,renYao == renYao2)#False，False
# print(renYao.__dict__ == renYao2.__dict__)#，不过他们的输出样子上是一样的,所以他们的属性是一样的
"""static就是谁都可以用，class和Instance都可以"""
print(Human.wusuowei(2))
# print(renYao.wusuowei(2))
print(renYao2.wusuowei(2))
print(nanRen.wusuowei(2))
