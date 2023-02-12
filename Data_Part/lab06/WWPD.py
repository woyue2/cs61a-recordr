from lab06 import *
t = tree(1, tree(2))
#______Your Answer

t = tree(1, [tree(2)])
#______Your Answer

label(t)
#______Your Answer

label(branches(t)[0])
#______Your Answer

x = branches(t)
len(x)
#______Your Answer

is_leaf(x[0])
#______Your Answer

branch = x[0]
label(t) + label(branch)
#______Your Answer

len(branches(branch))
#______Your Answer