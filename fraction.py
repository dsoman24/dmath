# Float to fraction calculator function.
# Walking the Stern-Brocot tree, within a given error.
# https://en.wikipedia.org/wiki/Stern%E2%80%93Brocot_tree#Mediants_and_binary_search
from floor_ciel import floor, ciel
from checkdp import cdp

def float_to_fraction(num, error = 0.00001):
    """
    Returns a tuple with the numerator and denominator of any float num as a fraction
    """
    # get decimal part of num:
    dec = num - floor(num)
    if dec == 0:
        return floor(num), 1
    nL, dL = 0, 1 # numerator1 and denominator1 respectively, lower bound. Starts at 0/1.
    nU, dU = 1, 1 # numerator2 and denominator2 respectively, upper bound. Starts at 1/1.

    while True: # while M is not in the range of the error of the number.
        nM = nL + nU
        dM = dL + dU
        M = nM/dM
        # In general,
        # nL/dL < mediant < nU/dU
        if M > dec+error: # if the mediant is too high, replace upper bound with mediant
            nU = nM
            dU = dM
        elif M < dec-error: # if the mediant is too low, replace lower bound with mediant
            nL = nM
            dL = dM
        else:
            numerator = nL + nU
            denominator = dL + dU
            return denominator*floor(num)+numerator, denominator # returns numerator and denominator

def fraction_string(numerator, denominator):
    """
    Returns a str in the form numerator/denominator. Arguments are ints. If denominator is 1 only str of numerator is returned.
    """
    if denominator == 1:
        return str(numerator)
    else:
        return str(numerator) + "/" + str(denominator)

def formatted_fraction(num, error = 0.00001):
    fractionTuple = float_to_fraction(num, error)
    return fraction_string(fractionTuple[0], fractionTuple[1])

if __name__ == "__main__":
    f1 = float_to_fraction(10/14+1/3)
    print(fraction_string(f1[0], f1[1]))