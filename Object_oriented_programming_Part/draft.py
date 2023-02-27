def order_weight(strng):
    """write the function to order the weight of a string"""
    l=list(strng.split())
    l=sorted(l)
    l=sorted(l, key=lambda x:sum(int(n) for n in str(x)))
    return " ".join(l)