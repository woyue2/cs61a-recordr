#放过我吧，你他妈自己的solution也报错啊，tree这里当我傻逼吧
def tree(label, branches=[]):
    for branch in branches:
        # assert is_tree(branch)
        return [label] + list(branches)

    
    
# Selectors
def label(tree):
    return tree[0]
def branches(tree):
    return tree[1:]
# For convenience
def is_leaf(tree):
    return not branches(tree)
# Write a function that returns the number of branches of a tree.
def num_branches(t):
    """Return the number of branches of a tree.
    >>> t = tree(1, [tree(2), tree(3)])
    >>> num_branches(t)
    2
    """
    if len(t) <= 1:
        return 0
    else:
        return len(t[1:])
# Write a function that returns the largest number in a tree.
def tree_max(t):
    """Return the maximum label in a tree.
    >>> t = tree(4, [tree(2, [tree(1)]), tree(10)])
    >>> tree_max(t)
    10
    """
    #
    return max([label(t)] + [tree_max(branch) for branch in branches(t)])
t = tree(4, [tree(2, [tree(1)]), tree(10)])
r = tree_max(t)
print(r)