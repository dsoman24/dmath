# Finding points of intersection of two functions using Newton's method.

from newtonsmethod import newtons_method

def poi(func1, func2, guess, iterations = 100):
    """Find points of intersection (POI) of two functions (func1, func2), starting from a guess.
    Computed over a given number of iterations (default 100).""" 
    def g(x):
        y = func1(x) - func2(x)
        return y
    
    x_nm = newtons_method(iterations, g, guess)
    return x_nm, func1(x_nm)
    