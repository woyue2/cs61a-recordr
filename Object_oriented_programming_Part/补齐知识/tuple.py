print(tuple('hello'))
# print(tuple(18,)) #不行
# 单元素元组
age = (18,)
# age = (18)
print(tuple(age))  # 可以
age = ('18', '18')
print(tuple(age))  # --> (18,18)
print(tuple(age).count(18))  # -->2
# 可读取
t = tuple(age)
print(type(t), t)
print(t[0])
print('-')
print('_'.join(t))#join里面是iterative但是也要
# lst = [1, 2]
lst = ['1', '2']
print('-'.join(lst))
#可便历
for i in t:
    print(',',i)
