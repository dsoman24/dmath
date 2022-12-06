from linalg import *

def markov(transition_matrix, init_vector, iterations):
    """Returns the probability vector after k iterations, given an initial state vector and transition matrix matrix"""
    final_matrix = matrix_exponent(transition_matrix, iterations)
    return matrix_multiply(final_matrix, init_vector)

m = markov(
    [
        [0.9, 0.3],
        [0.1,0.7]
    ],
    [
        [0.3],[0.7]
    ],
    3
)

print(m)