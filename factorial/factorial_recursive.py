# Recursive factorial

def rfactorial(n):
    """Returns the factorial of n (n!), where n is an integer."""
    if n == 0 or n == 1:
        return 1
    else:
        return n*rfactorial(n-1)