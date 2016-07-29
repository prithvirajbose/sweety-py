
# uses recursion
def sum(list):
    if len(list) == 1:
        return list[0]
    else:
        return list[0] + sum(list[1:])

def divide(array1, array2):
    """
    Divides array1 by array 2 and returns the result in another array.
    Raises RuntimeException if arrays sizes are unequal.
    """
    if len(array1) != len(array2):
        raise RuntimeError("Arrays should be of the same length")
    
    result = []
    
    for i in range(len(array1)):
        result.append(array1[i]/array2[i])

    return result

def byreftest(anynumber, anystring, anylist, anydict):
    anynumber *= 2 # multiply by 2

    anystring += "...something appended to the string"

    anylist.append('...append something to the list')
    
    del anydict[1] #delete the first key

if __name__ == '__main__':
    anynumber = 10
    anystring = 'hi how are you'
    anydict = {1: 20, 2: 30}
    anylist = [1,2,3]

    print '> before calling byreftest...'
    print anynumber
    print anystring
    print anydict
    print anylist

    byreftest(anynumber, anystring, anylist, anydict)

    print '> after calling byreftest...'
    print anynumber
    print anystring
    print anydict
    print anylist
