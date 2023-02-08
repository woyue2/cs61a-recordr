# Mutable Lists
# Background
"""
Let’s imagine you order a mushroom and cheese pizza from La Val’s, and
that they represent your order as a list:
>>> pizza = ['cheese', mushrooms']

A couple minutes later, you realize that you really want onions on the pizza.
Based on what we know so far, La Val’s would have to build an entirely new
list to add onions:
>>> pizza = ['cheese', mushrooms']
>>> new_pizza = pizza + ['onions'] # creates a new python list
>>> new_pizza
['cheese', mushrooms', 'onions']
>>> pizza # the original list is unmodified
['cheese', 'mushrooms']

This is silly, considering that all La Val’s had to do was add onions on top
of pizza instead of making an entirely new pizza.
We can fix this issue with list mutation. In Python, some objects, such
as lists and dictionaries, are mutable, meaning that their contents or state
can be changed over the course of program execution. Therefore, instead of
building a new pizza, we can just mutate pizza to add some onions!
>>> pizza.append('onions')
>>> pizza
['cheese', 'mushrooms', 'onions']
"""
# Realise
"""
1. append(el): Adds el to the end of the list
2. extend(lst): Extends the list by concatenating it with lst
3. insert(i, el): Insert el at index i (does not replace element but
adds a new one)
4. remove(el): Removes the first occurrence of el in list, otherwise errors
5. pop(i): Removes and returns the element at index i

We can also use the familiar indexing operator with an assignment statement
to change an existing element in a list. For example, let’s say you want to
replace mushrooms on your pizza with tomatoes. We can index into the list
at index 1 and reassign it to ’tomatoes’ like so:
>>> pizza[1] = 'tomatoes'
>>> pizza
['cheese', 'tomatoes', 'onions']

Although lists and dictionaries are mutable, many other objects, such as
numeric types, tuples, and strings, are immutable, meaning they cannot be
changed once they are created.
"""
#Box-and-Pointer Diagrams
"""
So far, we’ve been working with fairly simple lists whose contents we can
visualize in our heads. With the introduction of list mutation, programs
containing multiple list objects, especially nested lists, <become very difficult
to keep track of>.

To help us better visualize such programs, we can draw box-and-pointer
diagrams for lists. In a box-and-pointer diagram, each element in the list
goes into a box. The boxes are chained together to create a sequence. 
Primitive values, like numbers, are written directly into the box. Non-primitive
values, such as other lists, are drawn outside of the box and are pointed to
with an arrow. You can also label each box with its index to make it easier
to read.
"""

#WWPD
lst1 = [1, 2, 3]
lst2 = lst1
r = lst1 is lst2
print(r)#True

lst2.extend([5, 6])  #[1,2,3,5,6]
r = lst1[4]
print(r)#6

lst1.append([-1, 0, 1]) #不是[1,2,3,5,6,-1, 0, 1]
r = -1 in lst2#这个是True 和 False 不是index
print(r)#False
r = -1 in lst1
print(r)#False
print(lst1)#是[1, 2, 3, 5, 6, [-1, 0, 1]]

r = lst2[5]
print(r)#[-1, 0, 1]

lst3 = lst2[:] #lst3 是[1, 2, 3, 5, 6, [-1, 0, 1]]
r = lst3 is lst2
print(r)#False 用了[:]就是False了
lst3.insert(3, lst2.pop(3))#pop的是index，不是value
#lst2.pop(3) = [1, 2,  3, 6, [-1, 0, 1]]
#lst3 [1, 2, 3, [1, 2,  3, 6, [-1, 0, 1]] , 5 , 6, [-1, 0, 1]]

r = len(lst1)
print(lst1)
print(r)#6错了，是5

r = lst1[4] is lst3[6]
print(r)#True

r = lst3[lst2[4][1]]
print(r)#1

r = lst1[:3] is lst2[:3]
print(r)#True错了，是False
print(lst1[:3]) #[1, 2, 3]
print(lst2[:3]) #[1, 2, 3] == 不等于 is
r = (lst1[:3] == lst2[:3])
print(r)#True

r = lst1[:3] == lst3[:3]
print(r)#True

