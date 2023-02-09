from cats import *
from cats import autocorrect, lines_from_file

from cats import autocorrect, lines_from_file
r = autocorrect('testator', ['overrude' , 'toxicum'], lambda x, y, \
lim: min(lim + 1, abs(len(x) - len(y))), 8)
#                               8/8          7/8                    
# autocorrect('testator', ['impercipient', 'overrude', 'hyperingenuity', 'piligerous', 'molybdocolic', 'toxicum'], 
# lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 8)
'toxicum'
print(r)
# Error: expected
#     'overrude'
# but got
#     'toxicum'


qc=[r** 2 for r in range(4)]
print(qc)