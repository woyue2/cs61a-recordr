a = 10
b = 1
def func():
    a = 1
    b = 1
    return('a={}'.format(a))
func()
print(func())
print('a={}'.format(a))

# globals()
# print("globasl()", globals())
# print('---------------')
# locals()
print("locals()", locals())

