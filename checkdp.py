# Find number of decimal places in a float

def cdp(num):
    """Returns number of decimal places of a number"""
    num = str(num)   
    for i in range(0, len(num)):
        if num[i] == '.':
            return len(num[i+1:])
        else:
            return 0