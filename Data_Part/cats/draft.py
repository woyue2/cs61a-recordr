from cats import *
from cats import autocorrect, lines_from_file
# abs_diff = lambda w1, w2, limit: abs(len(w2) - len(w1))
# r = autocorrect("cul", ["culture", "cult", "cultivate"], abs_diff, 10)
first_diff = lambda w1, w2, limit: 1 if w1[0] != w2[0] else 0
r = autocorrect("wrod", ["word", "rod"], first_diff, 1)
'rod'

print(r)

# a = ['adfd']
# a = list(a)#-->['adfd']
# a = list(a[0])#-->['a', 'd', 'f', 'd']
# print(a)