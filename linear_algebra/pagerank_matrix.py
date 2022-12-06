from linalg import *

def googlematrix(P, a):
    """Calculate the google matrix G given a damping factor 'a', transition state matrix P.
    Uses formula G = aP + (1-a)K"""
    K = [[(1-a)/len(P)]*len(P) for i in range(len(P))]
    for i in range(len(P)):
        for j in range(len(P)):
            P[i][j] *= a

    return matrix_add(P, K)

if __name__ == "__main__":
    P = [
        [0,0,1,0,1/5],
        [1/3,0,0,1/2,1/5],
        [1/3,0,0,1/2,1/5],
        [1/3,1/2,0,0,1/5],
        [0,1/2,0,0,1/5]
    ]
    x = googlematrix(P, 0.85)
    #print(x)
    print_matrix(matrix_exponent(x, 100))
