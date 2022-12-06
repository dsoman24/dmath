# Iterative factorial

def ifactorial(n):
    """Returns the factorial of n (n!), where n is an integer."""
    if n == 0:
        return 1
    else:
        factorial = 1
        for i in range(1,n+1):
            factorial *= i
        return factorial