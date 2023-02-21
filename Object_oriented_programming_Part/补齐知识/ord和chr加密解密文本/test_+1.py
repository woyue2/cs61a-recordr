# a = input()
f = open('测试23.txt',encoding='utf-8')
content = f.read()
f.close

output = content
# print(output)
# print(type(output))
# print(content[1])
content = (list(content))
for i in range(len(content)):
    num = ord(content[i])
    str = chr(num-2)
    # print(str,i,num)
    content[i] = str
# print(content)
a = ''.join(content)
print(a)
f = open('测试23.txt','w')
f.write(a)
# f.close