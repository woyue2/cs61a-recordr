"""
Every Recursive function has three things.
1. One or more base cases
2. One or more ways to break the problem down into a smaller problem
• E.g. Given a number as input, we need to break it down into a smaller number
3. Solve the smaller problem recursively; from that, form a solution to the original proble
"""
# 1. What is wrong with the following function? How can we fix it?
"""
def factorial(n):
    return n * factorial(n)
"""
#死循环，改成return n * factorial(n-1)
#忽略了base！
def factorial(n):
    if n == 0:
        return 1#这里非常重要
    else:
        return n * factorial(n-1) 

# 2. Complete the definition for all_true, which takes in a list lst and returns True if there are no False-y
# values in the list and False otherwise. Make sure that your implementation is recursive
def all_true(lst):
    """
    >>> all_true([True, 1, "True"])
    True
    >>> all_true([1, 0, 1])
    False
    >>> all_true([])
    True
    """
    #your code here #不会做
    # 
    if not lst:
        return True
    elif not lst[0]:
        return False
    else:
        return all_true(lst[1:])
    

    

    
# 3. Write a function is_sorted that takes in an integer n and returns true if the digits of that number are
# nondecreasing from right to left.
def is_sorted(n):
    """
    >>> is_sorted(2)
    True
    >>> is_sorted(22222)
    True
    >>> is_sorted(9876543210)
    True
    >>> is_sorted(9087654321)
    False
    """
    # selector
    last1 = n % 10
    last2 = (n // 10) % 10
    # constructor    
    if len(str(n)) == 1:
        return True
    elif  last1 > last2:
        return False 
    else:
        return is_sorted(n//10)
    
    