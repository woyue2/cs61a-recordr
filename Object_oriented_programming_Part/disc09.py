class Tree:
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = branches
    def is_leaf(self):
            return not self.branches
"""WWPD"""
t0 = Tree(0)
t0.label
print("t0.label", t0.label ,0)
t0.branches
print("t0.branches", t0.branches, None) #错了是 []
# t1 = Tree(0, [1, 2]) # Is this a valid tree? False
t2 = Tree(0, [Tree(1), Tree(2, [Tree(3)])])
t2.branches[0]
print("t2.branches[0]", t2.branches[0], 0) # 错了是Tree object<__main__.Tree object at 0x000001953EC99400> 我错以为是label了……
t2.branches[1].branches[0].label
print("t2.branches[1].branches[0].label", t2.branches[1].branches[0].label ,None)#错了 是 3 懂了 1是second
print(__name__)
"""label是奇数的，加1，偶数不变"""
def make_even(t):
    """
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5)])
    >>> make_even(t)
    >>> t.label
    2
    >>> t.branches[0].branches[0].label
    4
    """
    #t is a Tree object
    t.label = t.label + 1 if t.label % 2 != 0 else t.label
    for b in t.branches:
        make_even(b)
t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5)])
make_even(t)
t.label
print("t.label", t.label)
t.branches[0].branches[0].label
print("t.branches[0].branches[0].label", t.branches[0].branches[0].label)
print('end')
"""所有label平方"""#看看答案，我debug出问题了
def square_tree(t):
    """Mutates a Tree t by squaring all its elements."""
    # if t.is_leaf():
    #     return
    # for b in t.branches:
    #     t.label = t.label ** 2
    #     return square_tree(b)
    t.label = t.label ** 2
    for b in t.branches:
        square_tree(b)

# t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5)])
# square_tree(t)
# print("square_tree(t)", square_tree(t.branches[0].label))
"""所有label的ave"""
def average(t):
    """
    Returns the average value of all the nodes in t.
    >>> t0 = Tree(0, [Tree(1), Tree(2, [Tree(3)])])
    >>> average(t0)
    1.5
    >>> t1 = Tree(8, [t0, Tree(4)])
    >>> average(t1)
    3.0
    """
    # def helper(counter,sum,t):
    #     sum += t.label
    #     for b in t.branches:
    #         counter += 1
    #         helper(counter,sum,b) #我只会传递参数，但是最后怎么变成平均数啊
    # return helper(1,0,t)
    def helper(t):
        total,count = t.label,1 # 这里的递归是用的for里面的递归
        for b in t.branches:    # 而不是用helper函数进行传参递归
            b_total,b_count = helper(b)
            total += b_total
            count += b_count
        return total,count
    total,count = helper(t)
    return total/count # 这里也不是return helper(t)说明之前我对内嵌的理解是不够深刻的

t0 = Tree(0, [Tree(1), Tree(2, [Tree(3)])])
average(t0)
print("average(t0)", average(t0))
###2 Mutable Functions in Python
#2.3
def memory(n):
    """
    >>> f = memory(10)
    >>> f = f(lambda x: x * 2)
    20
    >>> f = f(lambda x: x - 7)
    13
    >>> f = f(lambda x: x > 5)
    True
    """
    def helper(fn):
        nonlocal n
        print(fn(n))
        return helper#为了后面可以持续计算，持续用lamdba所以要return helper(fn)
    return helper
f = memory(10)
f = f(lambda x: x * 2)
print("f", f)
f = f(lambda x: x - 7)#如果不是return helper这里是 前一个结果整数是f,整数不调用lambda，是lambda调用整数
print("f", f)
"""2.4"""
def bathtub(n):
    """
    >>> annihilator = bathtub(500) # the force awakens...
    >>> kylo_ren = annihilator(10)
    >>> kylo_ren()
    490 rubber duckies left
    >>> rey = annihilator(-20)
    >>> rey()
    510 rubber duckies left
    >>> kylo_ren()
    500 rubber duckies left
    """
    def ducky_annihilator(rate): 
        def ducky():
            nonlocal n
            n = n - rate
            print(n, 'rubber duckies left')
        return ducky
    return ducky_annihilator
#
annihilator = bathtub(500)
kylo_ren = annihilator(10)
# kylo_ren()
print("kylo_ren()", kylo_ren())