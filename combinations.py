# Combinations of n choose k, where n >= k >= 0.

from factorial.factorial_iterative import ifactorial

def comb(n, k):
    """Combinations of n choose k, where n >= k >= 0."""
    if n >= k and k >= 0:
        return ifactorial(n)/(ifactorial(k)*ifactorial((n-k)))
    else:
        return None