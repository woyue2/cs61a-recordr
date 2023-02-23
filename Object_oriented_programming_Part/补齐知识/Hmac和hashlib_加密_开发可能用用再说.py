import hashlib

'''md5'''
str = '123456'
obj = hashlib.md5()  # Step 1步
obj.update(str.encode())  # Step 2步
str2 = hashlib.md5(str.encode())  # 1步到位
print('hash_md5:{}'.format(obj.hexdigest()))
print('hash_md5:{}'.format(str2.hexdigest()))
'''sha1'''
str2 = hashlib.sha1(str.encode())  # 1步到位
print('hash_sha1:{}'.format(str2.hexdigest()))
str2 = hashlib.sha256(str.encode())
print('hash_sha256:{}'.format(str2.hexdigest()))

import hmac
# 不会
# obj = hmac.new('123456'.encode('1'), digestmod='')
# r = obj.digest()
# print('hamc:{}', format(r))
# 先不管了