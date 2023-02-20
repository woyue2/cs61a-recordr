str = 'abc'
print(str[0])  # 字符串可以访问index但是不能mutate
print(str[1:])  # 甚至可以用slice
str = 'abcdefghijklmnl'
print(str[8:3:-1])  # ihgfe 8开始，走3步，-往右步进1
print(str[8:3:-2])  # ige   8开始，走3步，-往右步进2
print(str.find('l'))
print(str.find('p'))  # 无此字符则报错 输出-1
print(str.find('x'))  # 无此字符则报错 输出-1
print(str.index('l'))
# print(str.index('p')) 无此字符则报错 ValueError
# wait = input()
print((1 and 2))  # and是真则右传递
print((1 and 0))  # and是真则右传递
print((1 or 0))  # and是真则右传递 or是假的才会右传


class A(object):
    def __init__(self, a):
        self.b = a
