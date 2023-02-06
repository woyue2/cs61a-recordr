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

# 2. Complete the definition for all_true, which takes in a list lst and returns True if there are no False-y
# values in the list and False otherwise. Make sure that your implementation is recursive