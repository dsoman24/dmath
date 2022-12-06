import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from fraction import *
from random import randrange

#**********************************************************************************#
# Linear algebra sub-library of dmath library. This module contains many functions related
# to linear algebra. 
# Applications of these functions are in other files, contained in the linear_algebra folder. 

#**********************************************************************************#
# 1) Important operations

def copy_matrix(matrix):
    new_matrix = []
    for row in matrix:
        new_matrix.append(row[:])
    return new_matrix

# function to print matrix:
def print_matrix(matrix, decimal_places = 5, fraction = True):
    # Create a "deep" copy of the matrix:
    matrix = copy_matrix(matrix)
    # Turn entries into strings, floats to fractions, print rows. 
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = round(matrix[i][j], decimal_places)
            if fraction:
                matrix[i][j] = fraction_string(*float_to_fraction(matrix[i][j]))
            else:
                matrix[i][j] = str(matrix[i][j])
    for row in matrix:
        print(row)

def augment(lhs, rhs):
    """Create the augmeneted matrix [lhs | rhs]"""
    if len(lhs) != len(rhs):
        return None
    augmented = []
    for index, row in enumerate(lhs):
        augmented.append(row+rhs[index])
    return augmented

def identity(size):
    """Create the identity matrix of a given size"""
    matrix = [[0]*size for i in range(size)]
    for i in range(size):
        matrix[i][i] = 1
    return matrix

def un_augment(augmented, lhs_cols):
    """Returns the lhs and rhs of an augmented matrix"""
    lhs = []
    rhs = []
    for row in augmented:
        lhs.append(row[:lhs_cols])
        rhs.append(row[lhs_cols:])
    return lhs, rhs

def random_matrix(m, n, start, stop):
    """Generates a random m x n matrix with integer entries in the interval [start, stop)"""
    matrix = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(randrange(start, stop))
        matrix.append(row)
    return matrix

def transpose(matrix):
    """Returns the transpose of a matrix"""
    t_matrix = [[0]*len(matrix) for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            t_matrix[j][i] = matrix[i][j]
    return t_matrix

#**********************************************************************************#
# 2) Matrix and vector algebra oprations (multiplication, addition)

def matrix_add(*matrices):
    """Add matrices, assuming they are all the same size"""
    matrices = list(matrices)
    for i in range(len(matrices)):
        matrices[i] = copy_matrix(matrices[i])
    while len(matrices) > 1:
        second_matrix = matrices.pop(1)
        for i in range(len(matrices[0])):
            for j in range(len(matrices[0][0])):
                matrices[0][i][j] += second_matrix[i][j]
    return matrices[0]

def is_valid_matrix(matrix):
    rowlen = len(matrix[0])
    for row in matrix:
        if len(row) != rowlen:
            return False
    return True

def matrix_multiply(*matrices):
    """
    Multiply an arbitrary number of matrices. Returns the product matrix. 
    Returns none if matrix multiplication is not defined or matrices are invalid.
    """
    matrices = list(matrices)
    for i in range(len(matrices)):
        matrices[i] = copy_matrix(matrices[i])
    while len(matrices) > 1:
        # Get last 2 matrices, multiplication will be AB. B is last matrix, A is second to last. 
        A = matrices.pop(-2)
        B = matrices.pop(-1)
        if not is_valid_matrix(A) and is_valid_matrix(B): # Check if matrices are valid. 
            print("Entered matrices are not valid.")
            return None
        # mxn1 n2xp are dimensions of A, B respectively. Multiplication only defined if n1=n2.
        # The product at each iteration will be an mxp matrix. 
        m = len(A)
        n1 = len(A[0])
        n2 = len(B)
        p = len(B[0])
        if n1 != n2:
            print("Matrix multiplication is not defined") # Check if multiplication is defined. 
            return None
        product = [] # initialize product matrix to be the size of the new matrix (mxp). Initialized with all 0 entries.
        for i in range(m):
            product.append([0]*p)
        # Now multiply matrices using row-column rule.
        for i in range(m): # iterate through each row of A
            row = A[i]
            for j in range(p): # iterate through each column of B
                column = [] # Build column of jth column of B
                for k in range(n1):
                    column.append(B[k][j])
                dot_product = 0
                for idx in range(n1): 
                    # go through each entry in the selected row/column and get the dot product of the row and column.
                    dot_product += row[idx]*column[idx]
                    product[i][j] = dot_product
        matrices.append(product)
    return matrices[0]

def matrix_exponent(matrix, power):
    """Returns the square matrix A raised to some power"""
    matrices = [matrix for i in range(power)]
    return matrix_multiply(*matrices)

def scalar_multiply(scalar, matrix):
    """Returns the matrix multiplied by a scalar"""
    matrix = copy_matrix(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] *= scalar
    return matrix

def inner_product(v1, v2):
    """Calculate inner product of vectors v1 and v2"""
    return matrix_multiply(transpose(v1), v2)[0][0]

def norm(vector):
    """Returns the norm of a vector"""
    n = 0
    for i in vector:
        n += i[0]**2
    n **= 0.5
    return n

def dist(v1, v2):
    """Returns the distance between two vectors"""
    return norm(matrix_add(v1, scalar_multiply(-1, v2)))

def proj(vector, *basis):
    """Returns the orthogonal projection of a vector onto a subspace given its basis vectors."""
    vector = copy_matrix(vector)
    scalar = inner_product(vector, basis[0])/inner_product(basis[0], basis[0])
    projection = scalar_multiply(scalar, basis[0])
    for v in basis[1:]:
        scalar = inner_product(vector, v)/inner_product(v, v)
        scaled_basis = scalar_multiply(scalar, v)
        projection = matrix_add(projection, scaled_basis)
    return projection

def normalize(vector):
    scalar = 1/norm(vector)
    return scalar_multiply(scalar, vector)

def gram_schmidt(*basis): 
    """Given a basis for a subspace, return the orthogonal basis for that same subspace"""
    basis = list(basis)
    for i in range(len(basis)):
        basis[i] = copy_matrix(basis[i])
    ortho_basis = [basis[0]]
    for vector in basis[1:]:
        projection = proj(vector, *ortho_basis)
        ortho_vector = matrix_add(vector, scalar_multiply(-1, projection))
        #ortho_vector = normalize(ortho_vector)
        ortho_basis.append(ortho_vector) # normalizes the vector
    return ortho_basis

#**********************************************************************************#
# 3) Row operations

# elementary row oprations

def row_scale_return(idx, scalar, matrix):
    # Returns a copy of a scaled row given an index by a scalar, scalar cannot be 0.
    row = matrix[idx][:]
    if scalar != 0:
        for i in range(len(row)):
            row[i] *= scalar
    return row

def col_vector(matrix, current_row, idx):
    vector = []
    for i in range(current_row, len(matrix)):
        vector.append(matrix[i][idx])
    return vector

def row_swap(matrix, idx1, idx2):
        # Row indexing starts at 0. Swaps 2 rows given the index.
        # 'Permanent' operation
        row1 = matrix[idx1]
        row2 = matrix[idx2]
        matrix[idx1] = row2
        matrix[idx2] = row1
        return matrix

def move_to(matrix, which_idx, to_idx = -1):
    if to_idx == -1:
        to_idx = len(matrix)-1
    idx = which_idx
    while idx != to_idx:
        if which_idx > to_idx:
            nxt = -1
        else:
            nxt = 1
        matrix = row_swap(matrix, idx, idx+nxt)
        idx += nxt
    return matrix

def row_replace(matrix, which_idx, using_idx, scalar):
    # 'Permanent' operation, indexes are row indexes. 
    if scalar != 0:
        if which_idx != using_idx:
            scaled_row = row_scale_return(using_idx, scalar, matrix)
            for i in range(len(matrix[0])):
                matrix[which_idx][i] += scaled_row[i]
    return matrix

def row_scale(matrix, idx, scalar):
    # Scale a row of given index by a scalar, scalar cannot be 0.
    # 'Permanent' operation
    if scalar != 0:
        for i in range(len(matrix[0])):
            matrix[idx][i] *= scalar
    return matrix

# echelon function:

def echelon(matrix):
    matrix = copy_matrix(matrix)
    """Returns the echelon form of a matrix and a tuple of the pivot positions"""
    max_row_length = 0
    for i in range(len(matrix)):
        if len(matrix[i]) > max_row_length:
            max_row_length = len(matrix[i])
    for i in range(len(matrix)):
        if len(matrix[i]) < max_row_length:
            # if the length of each row is not consistent through the matrix, 
            # then 0s will be added to the end of the rows until they are all the same length.
            matrix[i] = matrix[i] + [0]*(max_row_length - len(matrix[i])) 
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    # 1. Reduce to echelon form
    pivot_positions = []
    current_row = 0
    while current_row < num_rows:
        #1.1. Move all 0 rows to the bottom. 
        zero_count = 0
        for i in range(num_rows):
            if matrix[i] == [0]*num_cols:
                zero_count += 1
        move_count = 0
        for i in range(num_rows):
            while matrix[i] == [0]*num_cols and move_count < zero_count: # keeps track of how many times it move 0's because it cannot move more rows than there are 0 rows. 
                # While the row is all zeroes, move to the bottom
                matrix = move_to(matrix, i)
                move_count += 1
        # 1.2. Find pivot column
        pivot_col_pos = -1 # -1 is placeholder for no pivot column
        for j in range(num_cols):
            column_vector = col_vector(matrix, current_row, j)
            if column_vector != [0]*(num_rows-current_row):
                pivot_col_pos = j
                for i in range(len(column_vector)): # move all rows with to position below a 0. 
                    if column_vector[i] == 0:
                        matrix = move_to(matrix, current_row + i)
                        break
                break
        if pivot_col_pos == -1:
            break # Basically if the submatrix is a 0 matrix, the matrix is reduced to echelon form.
        pivot_positions.append(pivot_col_pos)
        pivot_entry = matrix[current_row][pivot_col_pos]       
        if pivot_entry == 0:
            break # If the pivot entry is 0, that means a row of all 0s is reached and the matrix is reduced.
        # 1.3. Row replace with appropriate operation, make all entries below pivot a 0.
        for i in range(current_row, num_rows):
            scalar = -1*(matrix[i][pivot_col_pos]/pivot_entry) # Find appropriate scalar, which is -1*(entry at given row / pivot entry)
            matrix = row_replace(matrix, i, current_row, scalar)
        current_row += 1 # move on to next row, and find pivot there
    return matrix, tuple(pivot_positions)

# rref function from a function already in echelon form

def rref(matrix):
    """Returns the reduced row echelon form (rref) of a matrix."""
    matrix = copy_matrix(matrix)
    ech_form = echelon(matrix)
    matrix = ech_form[0]
    pivot_positions = ech_form[1]
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    # 2. Make echelon form to rref
    for col in pivot_positions:
        pivot_col = col_vector(matrix, 0, col)
        pivot_row = num_rows
        for i in range(len(pivot_col)-1, -1, -1):
            if pivot_col[i] != 0:
                pivot_row = i
                break
        pivot_entry = pivot_col[pivot_row]
        for i in range(len(pivot_col)-1, -1, -1):
            scalar = -1*(pivot_col[i]/pivot_entry)
            matrix = row_replace(matrix, i, pivot_row, scalar)
    for i in range(len(pivot_positions)):
        matrix = row_scale(matrix, i, 1/matrix[i][pivot_positions[i]])
    return matrix

# This is tough!
def solve(matrix):
    """Returns the solution x (size n x 1) to the system Ax=b, where A (size m x n) is a matrix and b (size m x 1) is a vector. 
    Input is an augmented matrix [A|b]
    Only works for systems with exactly one solution. 
    """
    r = rref(matrix)

        

def lu(matrix):
    """Returns the LU factorization of a matrix. First item returned is L, second is U.
    Also returns number of row swaps done in order to compute determinant. Each row swap is a multiplication by -1."""
    matrix = copy_matrix(matrix)
    max_row_length = 0
    for i in range(len(matrix)):
        if len(matrix[i]) > max_row_length:
            max_row_length = len(matrix[i])
    for i in range(len(matrix)):
        if len(matrix[i]) < max_row_length:
            # if the length of each row is not consistent through the matrix, 
            # then 0s will be added to the end of the rows until they are all the same length.
            matrix[i] = matrix[i] + [0]*(max_row_length - len(matrix[i])) 
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    lower = [[0]*num_rows for i in range(num_rows)] # lower triangular matrix, initialized as all 0's
    # 1. Reduce to echelon form
    pivot_positions = []
    current_row = 0
    lower_current_col = 0
    total_move_count = 0
    while current_row < num_rows:
        #1.1. Move all 0 rows to the bottom. 
        zero_count = 0
        for i in range(num_rows):
            if matrix[i] == [0]*num_cols:
                zero_count += 1
        move_count = 0
        for i in range(num_rows):
            while matrix[i] == [0]*num_cols and move_count < zero_count: # keeps track of how many times it move 0's because it cannot move more rows than there are 0 rows. 
                # While the row is all zeroes, move to the bottom
                matrix = move_to(matrix, i)
                move_count += 1**(num_rows-i)
        # 1.2. Find pivot column
        pivot_col_pos = -1 # -1 is placeholder for no pivot column
        for j in range(num_cols):
            column_vector = col_vector(matrix, current_row, j)
            if column_vector != [0]*(num_rows-current_row):
                pivot_col_pos = j
                for i in range(len(column_vector)): # move all rows with to position below a 0. 
                    if column_vector[i] == 0:
                        move_count += 1
                        matrix = move_to(matrix, current_row + i)
                        move_count += 1**(num_rows-(current_row+i))
                        break
                break
        total_move_count += move_count
        if pivot_col_pos == -1:
            break # Basically if the submatrix is a 0 matrix, the matrix is reduced to echelon form.
        pivot_positions.append(pivot_col_pos)
        pivot_entry = matrix[current_row][pivot_col_pos]
        if pivot_entry == 0:
            break # If the pivot entry is 0, that means a row of all 0s is reached and the matrix is reduced.
        # creates lower triangular matrix. Divides each entry in pivot column by entry and places column in a new matrix. 
        for i in range(current_row, num_rows):
            lower[i][lower_current_col] = matrix[i][pivot_col_pos]/pivot_entry
        # 1.3. Row replace with appropriate operation, make all entries below pivot a 0.
        for i in range(current_row, num_rows):
            scalar = -1*(matrix[i][pivot_col_pos]/pivot_entry) # Find appropriate scalar, which is -1*(entry at given row / pivot entry)
            matrix = row_replace(matrix, i, current_row, scalar)
        current_row += 1 # move on to next row, and find pivot there
        lower_current_col += 1
    upper = matrix
    return lower, upper, total_move_count

#**********************************************************************************#

# 4) Inverse matrices

# Interesting question to ask: how many n x nmatrices are invertible?

def det(matrix):
    """Compute the determinant of a square matrix"""
    if len(matrix) != len(matrix[0]):
        print("The determinant is only defined for square matrices!")
        return None
    factorization = lu(matrix)
    A = factorization[1]
    swaps = factorization[2]
    determinant = 1
    for i in range(len(A)):
        determinant *= A[i][i]
    determinant *= (-1) ** (swaps) # swapping rows 1 time negates the determinant. 
    return determinant

def inverse(matrix):
    """Returns the inverse of a matrix"""
    matrix = copy_matrix(matrix)
    if det(matrix) == 0:
        print("This matrix has no inverse/it isn't defined.")
        return None
    
    lhs_cols = len(matrix[0])
    num_rows = len(matrix)
    I = identity(num_rows)
    matrix = augment(matrix, I)
    num_cols = len(matrix[0])
    # 1. Reduce to echelon form
    pivot_positions = []
    current_row = 0
    while current_row < num_rows:
        #1.1. Move all 0 rows to the bottom. 
        zero_count = 0
        for i in range(num_rows):
            if matrix[i] == [0]*num_cols:
                zero_count += 1
        move_count = 0
        for i in range(num_rows):
            while matrix[i] == [0]*num_cols and move_count < zero_count: # keeps track of how many times it move 0's because it cannot move more rows than there are 0 rows. 
                # While the row is all zeroes, move to the bottom
                matrix = move_to(matrix, i)
                move_count += 1
        # 1.2. Find pivot column
        pivot_col_pos = -1 # -1 is placeholder for no pivot column
        for j in range(num_cols):
            column_vector = col_vector(matrix, current_row, j)
            if column_vector != [0]*(num_rows-current_row):
                pivot_col_pos = j
                for i in range(len(column_vector)): # move all rows with to position below a 0. 
                    if column_vector[i] == 0:
                        matrix = move_to(matrix, current_row + i)
                        break
                break
        if pivot_col_pos == -1:
            break # Basically if the submatrix is a 0 matrix, the matrix is reduced to echelon form.
        pivot_positions.append(pivot_col_pos)
        pivot_entry = matrix[current_row][pivot_col_pos]       
        if pivot_entry == 0:
            break # If the pivot entry is 0, that means a row of all 0s is reached and the matrix is reduced.
        # 1.3. Row replace with appropriate operation, make all entries below pivot a 0.
        for i in range(current_row, num_rows):
            scalar = -1*(matrix[i][pivot_col_pos]/pivot_entry) # Find appropriate scalar, which is -1*(entry at given row / pivot entry)
            matrix = row_replace(matrix, i, current_row, scalar)
        current_row += 1 # move on to next row, and find pivot there
        # 2. Make echelon form to rref
    for col in pivot_positions:
        pivot_col = col_vector(matrix, 0, col)
        pivot_row = num_rows
        for i in range(len(pivot_col)-1, -1, -1):
            if pivot_col[i] != 0:
                pivot_row = i
                break
        pivot_entry = pivot_col[pivot_row]
        for i in range(len(pivot_col)-1, -1, -1):
            scalar = -1*(pivot_col[i]/pivot_entry)
            matrix = row_replace(matrix, i, pivot_row, scalar)
    for i in range(len(pivot_positions)):
        matrix = row_scale(matrix, i, 1/matrix[i][pivot_positions[i]])

    return un_augment(matrix, lhs_cols)[1]

