from string_control import *

# print("ord('你'):", ord('你'))
# print("chr(20320):", chr(20320))
print("chr(20321):", chr(20321))
# print('bin(20320):',bin(20320))
# print('---------------------------------------------------------')
# print("('你').encode('gbk'):", ('你').encode('gbk'))
# print("('你').encode('utf-8'):", ('你').encode('utf-8'))
# print("('你').encode('big5'):", ('你').encode('big5'))
# print('---------------------------------------------------------')

print("code", code)
print("code.decode('gbk')", code.decode('gbk'))
# print("code.decode('utf-8')", code.decode('utf-8')) 报错

#’你好‘，utf-8编码，gbk解码，一个长度不够，两个字才够
print("code2.decode('gbk')", code2.decode('gbk'))
