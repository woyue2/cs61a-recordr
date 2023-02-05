lst = [2,3,6]
lst.append(9)
print(lst)#[2, 3, 6, 9]
lst.insert(0,1)
print(lst)#[1, 2, 3, 6, 9]
lst.extend([4])
print(lst)#[1, 2, 3, 6, 9, 4]
lst[1]=-lst[1]
print(lst)#[1, -2, 3, 6, 9, 4]
lst.pop(-1)#The only method here that has a return value is pop! All of the other methods return None.
print(lst)#[1, 2, 3, 6, 9]