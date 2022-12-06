from linalg import *

A = [[1,2], [2,1]]
B = [[9,8], [8,9]]

print_matrix(inverse(A))
print()
print_matrix(matrix_multiply(matrix_multiply(inverse(A), B), A))