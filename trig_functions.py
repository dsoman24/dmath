# Trigonometric functions computed by their Maclaurin series to a certain order

from factorial.factorial_iterative import ifactorial

# Compute this many terms in the series

def sin(x, order = 100):
    series = 0
    for n in range(order+1):
        series += (((-1)**n)/ifactorial(2*n+1))*x**(2*n+1)
    return series

def cos(x, order = 100):
    series = 0
    for n in range(order+1):
        series += (((-1)**n)/ifactorial(2*n))*x**(2*n)
    return series

def sec(x, order = 100):
    return 1/cos(x)

def cosec(x, order = 100):
    return 1/sin(x)

def tan(x, order = 100):
    return sin(x)/cos(x)

def arcsin(x, order = 100):
    series = 0
    for n in range(order+1):
        series += (ifactorial(2*n)/((4**n)*(ifactorial(n)**2)*(2*n+1)))*x**(2*n+1)
    return series

def arctan(x, order = 100):
    series = 0
    for n in range(order+1):
        series += (((-1)**n)/(2*n+1))*x**(2*n+1)
    return series

pi = 16*arctan(1/5) - 4*arctan(1/239)

def arccos(x, order = 100):
    return pi/2 - arcsin(x)