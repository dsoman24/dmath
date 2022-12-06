# Recursive fibonnaci algorithm. Returns the nth number in the fibonacci sequence

def rfib(n):
    """Returns the nth number in the Fibonacci sequence. By definition Fib(0) = 0 and Fib(1) = 1.
    Recursive algorithm."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return rfib(n-1)+rfib(n-2)

