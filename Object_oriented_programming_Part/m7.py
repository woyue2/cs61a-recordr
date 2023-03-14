class Tree:
    def __init__(self, label, branches=[]):
        self.label = label
        self.branches = branches
    def is_leaf(self):
        return not self.branches

"""
Implement tree_sum 
which takes in a Tree object 
and replaces the root value 
    with the sum of all the values in the tree. 
tree_sum should also 
    return the new root value"""
def tree_sum(t):
    if t.is_leaf():
        return t.label
    else:
        return t.label + tree_sum(t.branches[0]) + tree_sum(t.branches[1])
"""
"""
def double_tree(t):
    if t.is_leaf():
        t.branches = [Tree(t.label)]#人家直接构造内嵌，哪像我用什么append^
    else:
        for branche in t.branches:
            double_tree(branche)
        t.branches = [Tree(t.branches,t.branches)]#额我是无法理解太难了
