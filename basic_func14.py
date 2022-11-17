def main(a, b):
    from math import floor
    '''find the floor division of a and b and return it.
    
    Args:
        a (int): a number
        b (int): a number
        
    Returns:
        int: the result.
    '''
    d = floor(a/b)

    return d
print(main(11,2))