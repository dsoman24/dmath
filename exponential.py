# Exponential function by its maclaurin series to a specified number of terms.

from factorial.factorial_iterative import ifactorial
from logarithm import ln

def exp(x, order = 200):
    series = 0
    for n in range(order+1):
        series += (x**n)/(ifactorial(n))
    return series

e = exp(1) # Euler's number e

def expbase(base, x, order = 100, iterations = 10000):
    return exp(x*ln(base, iterations), order)

print(e)