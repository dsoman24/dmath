# Numerically compute the derivative of a function based on the limit definition of the derivative, using a small step size.
# Smaller step sizes will compute more accurate values for the derivative.

from checkdp import cdp

def d(f, x, step): # step = step size, f = function
    """Numerical approximation for the derivative of f, a function of x at the point x, with a given step size."""
    df = (f(x+step)-f(x))/step
    return df