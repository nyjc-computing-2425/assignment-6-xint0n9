from datetime import datetime
import time


# Part 1
def clock(n):
    '''
    digital clock on python
    '''
    for i in range(n):
        current_time = time.strftime("%H:%M:%S", time.localtime())
        print(current_time, end='\r')
        time.sleep(1)


#Part 2
def lcm(a,b):
    """
    find lowest common multiple
    """
    original_a = a
    original_b = b
    while True:
        if a == b:
            return a
        elif a < b:
            a += original_a
        else:
            b += original_b

# Part 3
def gcf(a, b):
    """
    find greatest common factor
    """
    if b == 0:
        return a
    while b != 0:
        a, b = b, a % b
    return a