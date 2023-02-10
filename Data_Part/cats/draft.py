from cats import match, fastest_words
p0 = [2, 2, 3]
p1 = [6, 1, 2]
r = fastest_words(match(['What', 'great', 'luck'], [p0, p1]))
print(r)