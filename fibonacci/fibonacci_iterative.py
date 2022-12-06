# Iterative fibonacci algorithm that returns the nth fibonacci number.

def ifib(n):
    """Returns the nth number in the Fibonacci sequence. By definition Fib(0) = 0 and Fib(1) = 1.
    Iterative algorithm."""
    seq = [0, 1] # by definition
    for i in range(2, n+1):
        seq.append(seq[-1]+seq[-2])
    return seq[n]