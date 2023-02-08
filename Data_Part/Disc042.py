"""
1.2 Write a function that takes in a value x, a value el, and a list and adds as
many el’s to the end of tht as there are x’s. Make sure to modify
the original list using list mutation techniques.
"""
def add_this_many(x, el, lst):
    """ Adds el to the end of lst the number of times x occurs
    in lst.
    >>> lst = [1, 2, 4, 2, 1]
    >>> add_this_many(1, 5, lst)
    >>> lst
    [1, 2, 4, 2, 1, 5, 5]
    >>> add_this_many(2, 2, lst)
    >>> lst
    [1, 2, 4, 2, 1, 5, 5, 2, 2]
    """
    # x in lst = 几次 ；加几个 el 在 lst后面 用append
    counter,i = 0,0
    while i< len(lst):
        if x == lst[i]:
            counter += 1
        i += 1
    for _ in range(counter):
        lst.append(el)
"""
1.3 Write a function that takes in a list and reverses it in place, i.e. mutate the
given list itself, instead of returning a new list.
"""
def reverse(lst):
    """ Reverses lst in place.
    >>> x = [3, 2, 4, 5, 1]
    >>> reverse(x)
    >>> x
    [1, 5, 4, 2, 3]
    """
    return lst.reverse() 