def a():
    print('1')
    def b():
        print('2')
        return '3'
    return b()
r = a()
print(r)