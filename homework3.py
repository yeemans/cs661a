def num_eights(pos):
    """Returns the number of times 8 appears as a digit of pos.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr'])
    True
    """
    "*** YOUR CODE HERE ***"
    
    if pos % 10 == 8:
        return 1 + num_eights(pos // 10)
    elif pos < 10: 
        return 0
    else:
        return num_eights(pos // 10)

def pingpongs(n): 
    # finds the number of ping pong numbers < n 
    # if this number is odd, we substract 
    # if even, we add
    pingpongs = 0
    largest_pingpong = 0
    for i in range(1, n): 
        if i % 8 == 0 or num_eights(i) >= 1: 
            pingpongs += 1
            largest_pingpong = i
    return [pingpongs, largest_pingpong]
print(pingpongs(100))
def pingpong(n):
    """Return the nth element of the ping-pong sequence.
    p
    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n <= 8: 
        return n
    # check if the last number is a pingpong number
    if pingpongs(n)[0] % 2 == 1: 
        return pingpong(n - 1) - 1
    else: 
        return pingpong(n - 1) + 1
        
    #print(distance)
   # if n > pingpong(n - distance): 
    #    return pingpong(n - distance) - distance 
    #return pingpong(n - distance) + distance
    
    
    
    
    
    if (n - 1) % 8 == 0 or num_eights(n - 1) >= 1: 
        if pingpong(n - 1) > pingpong(n - 2): 
            return pingpong(n - 2) - 1
        else: 
            return pingpong(n - 1) + 1
    #else: 
     #   if pingpong(n - 1) > pingpong(n - 2): 
      #      return pingpong(n - 1) + 1
       # else: 
        #    return pingpong(n - 1) - 1 
    
#print(last_pingpong(9))    

#print(pingpong(2))
print(pingpong(9))
#print(pingpong(16))
#print(pingpong(17))
#print(pingpong(100))
        
        
