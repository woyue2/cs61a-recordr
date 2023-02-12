# Constructor
def tree(label, branches=[]):
    # for branch in branches:
    for _ in range(len(branches)):
        # assert is_tree(branch)
        # return [label] + list(branches)
        return [label] + list(branches)
# Selectors
def label(tree):
    return tree[0]
def branches(tree):
    return tree[1:]
# For convenience
def is_leaf(tree):
    return not branches(tree)
########################################################################
t = tree(1,
        [tree(3,
             [tree(4),
              tree(5),
              tree(6)]),
         tree(2)])
print(t)#[1, [3, None, None, None], None]---None意味着是leaf没有branch
#----------WWPD--------------#
r = label(t)#1
# print(r)
r = t[0]#1
# print(r)
r = label(branches(t)[0])
# print(r)
r = t[1:][1]#-->None
# r = is_leaf(t[1:][1])-->報錯
# print(r)
# r = [label(b) for b in branches(t)]#3,None 但是None沒有那個[0]
# print(r)-->報錯
# r = branches(tree(5, [t, tree(3)]))#輸出t
# r = branches(tree(5, [t, tree(3)]))[0]#輸出t
r = branches(tree(5, [t, tree(3)]))[0][0]#輸出1,第一個[0]去了t，第二個[0]去了1
# print(r)