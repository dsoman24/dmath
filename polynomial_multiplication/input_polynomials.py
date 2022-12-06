# Input and interpret a polynomial in the form a1x^i1+a2x^i2+a3x^i3+...
from multiply_polynomials import polymult, polydisp

numbersstr = [str(i) for i in range(0, 10)]
numbersint = [i for i in range(0, 10)]

def countinstance(string, char):
    count = 0
    string = str(string)
    char = str(char)
    for i in string:
        if i == char:
            count += 1
    return count

def highestindex(polynomial):
    """Polynomial arg is a string (in form a1x^i1+a2x^i2+a3x^i3+...), will return the highest index"""
    polynomial = polynomial+'.'
    if 'x' not in polynomial:
        highestindex = 0
    if 'x' in polynomial and '^' not in polynomial:
        highestindex = 1
    else:
        highestindex = 0
        for i in range(len(polynomial)):
            indexint = 0
            if polynomial[i] == '^':
                indexeval = polynomial[i+1:]
                for n in range(len(indexeval)):
                    if indexeval[n] not in numbersstr:
                        try:
                            indexint = int(indexeval[:n])
                        except ValueError:
                            indexint = 0
                            break
                        else:
                            if indexint > highestindex:
                                highestindex = indexint
                            break
    return highestindex

# while True:
#     polyinp = input("Enter the polynomial product to evaluate: ")
#     if polyinp.lower() == 'q':
#         break

#     polyinp.replace(' ', '')
#     polylist = []

#     start = 0 
#     end = 0
#     individualpoly = []
#     for i in range(len(polyinp)):
#         if polyinp[i] == ')' or polyinp[i] == ']':
#             end = i
#             individualpoly = polyinp[start+1:end]
#             polylist.append(individualpoly)
#             start = i+1
   
#     print(polylist)

#     # want: 
#     # [[a1, a2, a3, ..., an], [b1, b2, b3, ..., bn], ...]
#     # also consider input [ax+bx] for example, and add a+b in the index in position 1.
#     # eventually make it so that the variable can be any single character, not just x 

#     productlist = []
#     for polynomial in polylist:
#         coefficients = [0]*(highestindex(polynomial)+1) # [0]*highest index, intializes list with 0's
#         terms = []
#         start = 0
#         end = 0
#         polynomial += '+'
#         for i in range(len(polynomial)):
#             if polynomial[i] == '+' or polynomial[i] == '-':
#                 end = i
#                 term = polynomial[start:end]
#                 terms.append(term)
#                 start = i
#         for term in terms:
            