# Logarithm base e based on numerical integration. 

from eulers_method import eulers_method

def ln(x, iterations = 1000):
    """iterations = number of iterations to compute the value of ln(x) to certain degree of accuracy."""
    def f(z, w):
        return 1/z
    return eulers_method(iterations,(x-1)/iterations, 1, 0, f)[1][-1]

def logbase(x, base, iterations = 1000):
    return ln(x, iterations)/ln(base, iterations)