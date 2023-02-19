# super(B, self) 现在一般简写为super()
class A(object):
    def __init__(self):
        print("enter A")
        print(self)  # this will print <__main__.D object at 0x...>
        print("leave A")
class B(A):
    def __init__(self):
        print("enter B")
        print(self)  # this will print <__main__.D object at 0x...>
        super(B, self).__init__()
        print("leave B")
class C(A):
    def __init__(self):
        print("enter C")
        print(self)  # this will print <__main__.D object at 0x...>
        super(C, self).__init__()
        print("leave C")
class D(B, C):
    pass

d = D()