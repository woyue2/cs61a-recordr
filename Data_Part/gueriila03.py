from math import pow
#Question 2 start
def rational_pow(x, e):
    """
    >>> r = rational_pow(rational(2, 3), 2)
    >>> numer(r)
    4
    >>> denom(r)
    9
    >>> r2 = rational_pow(rational(9, 72), 0)
    >>> numer(r2)
    1
    >>> denom(r2)
    1
    """
    return [pow(x[0],e),pow(x[1],e)]
#constructor start
def rational(a,b):
    return [a,b]
def numer(a):
    return int(a[0])
def denom(a):
    return int(a[1])
#constructor end
#Question 2 end
''
#Question c start
# function factorial start -- n!
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
# function factorial end
# function approx_e start --#calculate e = sum(1/n!) n 从0开始
def approx_e(iter):#iter should bu assumed as 100000 then the basis is ok
    if iter == 0:
        add = 1
        return add
    else:
        add =  1/factorial(iter)
        return add + approx_e(iter - 1)
# function approx_e end
#debug start
print(approx_e(993))#不能写999 超出最大depth
# debug end  result  2.7182818284590455
#Question c end
''
## Tree Start
def tree(label, branches = []):
    for b in branches:
        assert is_tree(b), 'branches must be trees'
    return [label] + list(branches)
def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for b in branches(tree):
        if not is_tree(b):
            return False
    return True
def label(tree):
    return tree[0]
def branches(tree):
    return tree[1:]
def is_leaf(tree):
    '''if len(tree) == 1:我的傻鸟代码啊
        return True
    for b in branches(tree):
        if not is_leaf(b):
            return False'''
    return not branches(tree)#有branch的就不是leaf,没有branch的就是leaf
# Question b Start
# min_heap start 子比母大
def is_min_heap(t):
    for b in branches(t):
        if label(t) > label(b) or not is_min_heap(b):#这里就已经在递归了，很强
            return False
    return True   
# min_heap end 抄的，因为已经看了答案
# largest_product_path Start 路径label乘积起来最大的，输出乘积
def largest_product_path(tree):#tree是list，label非负数
    """
    >>> largest_product_path(None)
    0
    >>> largest_product_path(tree(3))
    3
    >>> t = tree(3, [tree(7, [tree(2)]), tree(8, [tree(1)]), tree(4)])
    >>> largest_product_path(t)
    42
    """
    '''Stupid and Wrong Code
    if not True:
        return 0
    elif is_leaf(tree):
        return label(tree)
    else:
        now_label = label(tree)
        # now_branch = branches(tree)
        next_label = [label(now_branch) for now_branch in branches(tree) if True]
        now_list = [value * now_label for value in next_label]
        largest_product_path(branches(tree))
        #idea:把所有可能乘积存入一个list，用max来提取
        paths = [ _________________________________________________________ ]
        return _______________________________'''
    if not tree:
        return 0
    elif is_leaf(tree):
        return label(tree)
    else:
        paths = [largest_product_path(t) for t in branches(tree)]
        return label(tree) * max(paths)#我懂了，因为每一层都会自己传递最大的值上来，递归是先进进到最后，再一层层返回！
#  largest_product_path End TooDifficultForMe 抄的因为我不会
# Question b End
## Tree End