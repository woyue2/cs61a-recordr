from cats import about,choose
from utils import *
# ps = ['hi', 'how are you', 'fine']
# s = lambda p: len(p) <= 4
# # r = choose(ps, s, 0)
# # r = choose(ps, s, 1)
# r = choose(ps, s, 2)
# print(r)
  
# about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
# r = choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
# r = choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
# dogs = about(['dogs', 'hounds'])
# r = dogs('A paragraph about cats.')
# print(r)#'Cute Dog!'
# r = split(lower(remove_punctuation('Cute Dog!')))
# print(r)-->['cute', 'dog']
# print('a' in ['a','b'])
# r = bool([])
# print(r)

# lst = [1,2,3]
# r = lst.pop()
# print(r)
# print(lst)

# dogs = about(['dogs', 'hounds'])
# r = dogs('A paragraph abouct cats.')
# print(r)

# a = 1
# b = [1,2]
# r = b[-1]
# print(r)
# b.pop()
# print(b)
from cats import about
from cats import choose
dogs = about(['dogs', 'hounds'])
r = dogs('A paragraph about cats.')
print(r)