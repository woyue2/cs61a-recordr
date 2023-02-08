def tree(label,branches=[]):
    # for b in branches:
    #     assert is_tree(b),'branches must be trees'
    return [label] + list(branches)
    #what the hell将会输出?
def label(tree):
    return tree[0]
def branches(tree):
    return tree[1:]
a = [1,2]
b = [0]
r = list(b + a)
r1 = b+a
print('--------')
print(r)
print(r1)