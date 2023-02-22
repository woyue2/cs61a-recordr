num = input(',分：')
a = num.split(',')
print(a)
print(type(a))
r = [int(ele) for ele in a]
print("r", r)

# lst = []
# while True:
#     i = int(input('a'))#
#     print(f'adf{type(i)}')
#     if  str(i) == 'exit':
#         break
#     lst.append(i)
#     print(type(i))
# print(lst)