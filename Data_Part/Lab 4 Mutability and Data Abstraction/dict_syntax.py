artists = {
   'Ariana Grande': 'No Tears Left To Cry',
   'Marshmello': 'FRIENDS',
   'Migos': ['Stir Fry', 'Walk It Talk It']
}
r = artists
print(r)
# add
artists['new'] = 'luoli'
r = artists
print(r)
#in 是判断 有没有主键，而不是值
print('new' in artists)#True 
print('luoli' in artists)#False
#
print('------')
print(r.keys())
print(r.values())
#
print('------')
#每一行的 key+ value 都加上()变成 tuple的元素
print(r.items())