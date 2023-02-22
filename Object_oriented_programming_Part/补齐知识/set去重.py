# set = {1,2,3}
# print("set", set)
# set2 = {3,4,5}
# list(set)
# print("list(set)", list(set))
# print("list(set2)", list(set2))
# list(set)+list(set2)
# print("list(set)+list(set2)", list(set)+list(set2))
# # set(list(set)+list(set2))
# # print("set(list(set)+list(set2))", set(list(set)+list(set2)))

lst = [55,6,7,1,7]
print("lst", lst)
r = set(lst)
print("set(lst)", r)
s = list(r)
print("r", s)
s.sort(reverse=True)
print("s", s)
s.sort(reverse=False)
print("s", s)
