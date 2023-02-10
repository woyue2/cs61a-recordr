a = "cats"
b = "scat"
 # cats --add 's'--> scats --del 's'-> scat
lsta = list(a)#['c', 'a', 't', 's'] 
lstb = list(b)#['s', 'c', 'a', 't']
#lsta insert lstb[0],del lsta [-1]
print(lsta,lstb)


# cats -> scats
#找一样的？
