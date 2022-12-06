# Numerically approximate the value of a function using the specified order of its Taylor series expension.

from factorial.factorial_iterative import ifactorial
from derivative.derivative_nth import dn

def taylor(f, x, a, order, step):
    """Use the taylor expansion around x=a for f, a function of x, up to a given order 
    to approximate the value of the function. Useful for finding values of non-primitive (?) functions, like trig functions.
    Step parameter is the step length for computing the derivative. """
    
    series = 0
    for n in range(0, order+1):
        series += (dn(f, a, n, step)/ifactorial(n))*(x-a)**n
    
    return series
