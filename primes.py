# Very basic prime generator

def primes(N):
    """Finds all prime numbers iteratively from 0 to N"""
    primelist = []
    for n in range(1, N):
        prime = True
        if n == 1:
            prime = False
        else:
            for i in range(2, n):
                if n % i == 0:
                    prime = False
                    break
        if prime == True:
            primelist.append(n)
    return primelist

    
print(primes(1))