# Numerical differentiation to find the nth derivative of a function f(x), so f^(n)(x). 
# From the limit definition of a derivative: https://en.wikipedia.org/wiki/Numerical_differentiation#Higher_derivatives

from combinations import comb

def dn(f, x, n, step):
    """Numerically approximate the nth derivative of f, a function of x, with a given step size.
    Only natural number order derivatives."""
    if n >= 0:
        sum_component = 0
        for k in range(n+1):
            sum_component += ((-1)**(k+n))*comb(n, k)*f(x+k*step)
        return (step**(-n))*sum_component
    else:
        return None