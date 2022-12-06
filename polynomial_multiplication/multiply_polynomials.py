# Polynomial Multiplier algorithm for an arbitrary number of polynomials
# in the form:
# a_0x^0+a_1x^1+a_2x^2+...+a_nx^n
# arguments are lists where each item is the coefficient of x^index:
# [a_0, a_1, a_2, ... , a_n], list of length n+1

def polymult(*polynomials):
    """Argument is an arbitrary number of list interpretations of a polynomial. Will return the product
    as a list interpretation of a polynomial"""
    # turns tuple into list of polynomials
    polys = list(polynomials) 
    # loops until only 1 polynomial remains, which is the final product
    while len(polys) > 1: 
        # product without adding like terms
        prod = [] 
        # iterates through each term in the polynomial in index 0, 
        # applies distributive property with polynomial in index 1
        for a in range(len(polys[0])): 
            for b in range(len(polys[1])): 
                # tuple in the form (product of coefficients, 
                # sum of index (power of x)):
                coefindex = (polys[0][a]*polys[1][b], a+b) 
                prod.append(coefindex)
        # product after adding like terms:
        finalprod = [] 
        # highest degree of the polynomial:
        n = len(polys[0])+len(polys[1])-2 
        # from x^0 to x^n sums all coefficients of like terms
        ind = 0 # current index
        while ind <= n: 
            coefadd = 0 
            for i in prod: 
                if i[1] == ind:
                    coefadd += i[0]
            finalprod.append(coefadd)
            ind += 1 
        # adds product to the beginning of the list of polynomials, slices 
        # first two polynomials from list. Shortens polynomial list until 1.
        polys = [finalprod] + polys[2:] 
    return polys[0]

def polydisp(polynomial):
    """Displays polynomial given a list interpretation"""
    p = ""
    for i in range(len(polynomial)):
        if polynomial[i] == 0:
            continue
        else:
            p += str(polynomial[i])
            if i > 0:
                p += 'x'
            if i > 1:
                p += '^' + str(i)
            if i < len(polynomial) - 1:
                p += ' + '
    print(p)