# Constructor
def tree(label, branches=[]):
    if branches == []: 
        return [label]
    else:
        return [label] + branches
# Selectors
def label(tree):
    return tree[0]
def branches(tree):
    return tree[1:]

number_tree = tree(1,
         [tree(2,[]),
          tree(3,
               [tree(4),
                tree(5)]),
          tree(6,
               [tree(7)])])
# print('DEbug:',number_tree)

def acorn_finder(t):
    """Returns True if t contains a node with the value 'acorn' and
    False otherwise.

    >>> scrat = tree('acorn')
    >>> acorn_finder(scrat)
    True
    >>> sproul = tree('roots', [tree('branch1', [tree('leaf'), tree('acorn')]), tree('branch2')])
    >>> acorn_finder(sproul)
    True
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> acorn_finder(numbers)
    False
    """
    "*** YOUR CODE HERE ***"
    # 访问label值-->label数值是不是等于'acorn'-->是，True，否,False
    # TF = label(t)
    # if len(t) == 1:
    #     if TF == 'acorn':
    #         return True
    #     else:
    #         return False
    # else:
    #     if TF == 'acorn':
    #         return True
    #     else:
    #         return (acorn_finder(el) for el in branches(t) if t) 
    if(label(t)=='acorn'):
      return True 

    for b in branches(t):
      if(acorn_finder(b)):
        return True 
    return False 
#debug
sproul = tree('roots', [tree('branch1', [tree('leaf'), tree('acorn')]), tree('branch2')])
pr = acorn_finder(sproul)
print(pr)