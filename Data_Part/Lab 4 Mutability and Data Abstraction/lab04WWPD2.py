pokemon = {'pikachu': 25, 'dragonair': 148, 'mew': 151}
r = pokemon['pikachu']
print(r)#25

r = len(pokemon)
print(r)#3

pokemon['jolteon'] = 135#add
pokemon['mew'] = 25#change
r=len(pokemon)
print(r)#4 


r = 'mewtwo' in pokemon
print(r)#False

r ='pikachu' in pokemon
print(r)#True

r = 25 in pokemon
print(r)#False

r = 148 in pokemon.values()#后面还有values！
print(r)#True

r = 151 in pokemon.keys()
print(r)#False

r = 'mew' in pokemon.keys()
print(r)#True

pokemon['ditto'] = pokemon['jolteon']#将右边的值赋予左边
r = pokemon['ditto']
print(r)#135
