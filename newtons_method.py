# Newton's method to approximate roots and points of intersection of two equations

from derivative.derivative_first import d

def newtons_method(iterations, f, guess):
    """Newton's method to solve for the roots of a function f, with an initial guess."""
    i = 0
    x = guess
    while i < iterations:
        x -= f(x)/d(f, x, 0.00001)
        i += 1

    return x