# Using Euler's method to numerically solve a differential equation in the form dy/dx = f(x, y)
# y_(n+1) = y_n+h*f(x_n, y_n)
# where h is the step length, and x_(n+1) = x_n+h

def eulers_method(iterations, step, xn, yn, func): 
    """n is number of iterations, step is step length, xn is initial x, yn is initial y, func is the derivative function f(x, y)."""
    xvals = [xn]
    yvals = [yn]

    steps = 0
    while steps < iterations:
        xn += step
        yn += step*func(xn, yn)
        xvals.append(xn)
        yvals.append(yn)
        steps += 1
    return xvals, yvals # returns the lists of x and y values over the iteration

