"""
CMPSC448 Machine Learning and AI Homework 4a
Matrices From Scratch
Author: Joseph Sepich (jps6444)
"""

def question_matvec(mat, vec):
    """Performs matrix vector multiplication.

    Arguments:
       mat {list[list]} -- m by n matrix
       vec {list} -- m by 1 column vector

    Returns:
       result {list} -- column vector result
    """
    # Check dimensions
    row_mat = len(mat)
    col_mat = len(mat[0])
    row_vec = len(vec)
    if col_mat != row_vec:
        raise Exception('Dimension Mismatch')
    result = []
    for row in range(row_mat):
        row_sum = 0
        for col in range(col_mat):
            try:
                row_sum += mat[row][col] * vec[col]
            except:
                raise Exception('Dimension Mismatch')
        result.append(row_sum)

    return result


def question_matmat(mat1, mat2):
    """Performs matrix multiplication

    Arguments:
        mat1 {list[list]} -- m by n matrix
        mat2 {list[list]} -- n by p matrix

    Returns:
        result {list[list]} -- resulting matrix
    """
    row_mat1 = len(mat1)
    col_mat1 = len(mat1[0])
    row_mat2 = len(mat2)
    col_mat2 = len(mat2[0])
    if col_mat1 != row_mat2:
        raise Exception('Dimension Mismatch')
    result = []
    for col in range(col_mat2):
        # get col vector from mat2
        vec = []
        for row in mat2:
            vec.append(row[col])
        # multiply col vector from mat1 * vec
        new_col = question_matvec(mat1, vec)
        for row in range(len(new_col)):
            try:
                result[row].append(new_col[row])
            except:
                result.append([])
                result[row].append(new_col[row])
    return result

def question3(A, W, x, b):
    """Finds the derivative of (Ax-b)'W(Ax-b)

    Arguments:
        A {list[list]} -- matrix
        W {list[list]} -- matrix
        x {list} -- vector
        b {list} -- vector

    Returns:
        list -- derivative
    """
    # function is (Ax-b)'W(Ax-b))
    # derivative is (A'W+A'W')(Ax-b)
    coeff = question_matvec(A, x)
    coeff = vector_addition(coeff, b, subtract=True)
    A_prime = transpose(A)
    W_prime = transpose(W)
    left_term = question_matmat(A_prime, W)
    right_term = question_matmat(A_prime, W_prime)
    term = matrix_addition(left_term, right_term)
    return question_matvec(term, coeff)


def question4(A, C, W, x, b, d):
    """Finds the derivative of (Ax-b)'W(Cx-d)

    Arguments:
        A {list[list]} -- matrix
        C {list[list]} -- matrix
        W {list[list]} -- matrix
        x {list} -- vector
        b {list} -- vector
        b {list} -- vector

    Returns:
        list -- derivative
    """
    # function is (Ax-b)'W(Cx-d)
    # derivative is A'W(Cx-d)+C'W'(Ax-b)
    coeff_right = question_matvec(A, x)
    coeff_right = vector_addition(coeff_right, b, subtract=True)
    coeff_left = question_matvec(C, x)
    coeff_left = vector_addition(coeff_left, d, subtract=True)
    A_prime = transpose(A)
    W_prime = transpose(W)
    C_prime = transpose(C)
    left_term = question_matmat(A_prime, W)
    right_term = question_matmat(C_prime, W_prime)
    left_term = question_matvec(left_term, coeff_left)
    right_term = question_matvec(right_term, coeff_right)
    return vector_addition(left_term, right_term)

def question5(A, x, sigmoid):
    """Finds the derivative of (Asig(x))^2

    Arguments:
        A {list[list]} -- matrix
        x {list} -- vector
        sigmoid {function} -- sigmoid function

    Returns:
        list -- derivative
    """
    # function is (Asig(x)).^2
    # derivative is 2A'(Asig(x))d_sig(x)
    # recall sig deriv = sig(x) * (1 - sig(x))
    A_prime = transpose(A)
    A_prime = scalar_mult(2, A_prime)
    result = question_matmat(A_prime, A)
    result = question_matvec(result, func_vec(sigmoid, x))
    for row in range(len(result)):
        result[row] = result[row] * sigmoid(x[row]) * (1 - sigmoid(x[row]))
    return result

def question6(A, x, b, sigmoid):
    """Finds the derivative of (sig(Ax)-b)^2

    Arguments:
        A {list[list]} -- matrix
        x {list} -- vector
        b {list} -- vector
        sigmoid {function} -- sigmoid function

    Returns:
        list -- derivative
    """
    # function is (sig(Ax)-b).^2
    # derivative is 2A'((sig(Ax)-b)*d_sig(Ax))
    # recall sig deriv = sig(x) * (1 - sig(x))
    A_prime = transpose(A)
    A_prime = scalar_mult(2, A_prime)
    A_x = question_matvec(A, x)
    sig_ax = func_vec(sigmoid, A_x)
    d_sig_ax = func_vec(lambda z: sigmoid(z) * (1 - sigmoid(z)), A_x)
    result = []
    for row in range(len(sig_ax)):
        result.append((sig_ax[row] - b[row]) * d_sig_ax[row])
    return question_matvec(A_prime, result)

def question7(A, W, x, b, sigmoid):
    """Finds the derivative of (Wsig(Ax)-b)^2

    Arguments:
        A {list[list]} -- matrix
        W {list[list]} -- matrix
        x {list} -- vector
        b {list} -- vector
        sigmoid {function} -- sigmoid function

    Returns:
        list -- derivative
    """
    # function is (Wsig(Ax)-b)^2
    # derivative is 2A'(W'(Wsig(Ax)-b))*d_sig(Ax))
    A_prime = transpose(A)
    A_prime = scalar_mult(2, A_prime)
    A_x = question_matvec(A, x)
    sig_ax = func_vec(sigmoid, A_x)
    d_sig_ax = func_vec(lambda z: sigmoid(z) * (1 - sigmoid(z)), A_x)
    W_result = question_matvec(W, sig_ax)
    for row in range(len(W_result)):
        W_result[row] = W_result[row] - b[row]
    W_prime = transpose(W)
    W_result = question_matvec(W_prime, W_result)
    for row in range(len(W_result)):
        W_result[row] *= d_sig_ax[row]
    return question_matvec(A_prime, W_result)

def question8(A, W, x, b, sigmoid, huber):
    """Finds the derivative of huber(sig(Ax)-b)

    Arguments:
        A {list[list]} -- matrix
        W {list[list]} -- matrix
        x {list} -- vector
        b {list} -- vector
        sigmoid {function} -- sigmoid function
        huber {function} -- huber function

    Returns:
        list -- derivative
    """
    # function is huber(sig(Ax)-b)
    # derivative is d_hub(sig(Ax)-b)d_sig(Ax)
    A_x = question_matvec(A, x)
    sig_ax = func_vec(sigmoid, A_x)
    for row in range(len(sig_ax)):
        sig_ax[row] -= b[row]
    # huber d
    d_hub = []
    for row in range(len(sig_ax)):
        x = sig_ax[row]
        x_abs = abs(x)
        if x_abs > 1:
            d_hub.append(x / x_abs)
        else:
            d_hub.append(x)
    d_sig_ax = func_vec(lambda z: sigmoid(z) * (1 - sigmoid(z)), A_x)
    for row in range(len(d_hub)):
        d_hub[row] *= d_sig_ax[row]
    d_hub = question_matvec(transpose(A), d_hub)
    return d_hub

def matrix_addition(A, B, subtract=False):
    """Matrix addition

    Arguments:
        A {list[list]} -- matrix
        B {list[list]} -- matrix

    Keyword Arguments:
        subtract {bool} -- is subtraction (or addition) (default: {False})

    Returns:
        list[list] -- A + B
    """
    result = A[:][:]
    for row in range(len(A)):
        for col in range(len(A[0])):
            if subtract:
                result[row][col] = A[row][col] - B[row][col]
            else:
                result[row][col] = A[row][col] + B[row][col]
    return result

def vector_addition(x, b, subtract=False):
    """Vector addition

    Arguments:
        x {list} -- vector
        b {list} -- vector

    Keyword Arguments:
        subtract {bool} -- is subtraction (or addition) (default: {False})

    Returns:
        list -- x + b
    """
    result = x[:]
    for i in range(len(x)):
        if subtract:
            result[i] = x[i] - b[i]
        else:
            result[i] = x[i] + b[i]
    return result

def transpose(A):
    """Transpose the given matrix

    Arguments:
        A {list[list]} -- matrix

    Returns:
        list[list] -- A'
    """
    A_prime = []
    for col in range(len(A[0])):
        A_prime.append([])
    new_row = 0
    for col in range(len(A[0])):
        for row in range(len(A)):
            A_prime[new_row].append(A[row][col])
        new_row += 1
    return A_prime

def scalar_mult(const, A, vec=False):
    """Multiples list struct by scalar

    Arguments:
        const {double} -- scalar
        A {list[list?]} -- matrix or vector

    Keyword Arguments:
        vec {bool} -- whether A is vector or matrix (default: {False})

    Returns:
        list[list?] -- matrix of vector
    """
    if vec:
        result = A[:]
    else:
        result = A[:][:]
    for row in range(len(A)):
        if vec:
            result[row] = const * A[row]
        else:
            for col in range(len(A[0])):
                result[row][col] = const * A[row][col]
    return result

def func_vec(func, vec):
    """Element wise function runner

    Arguments:
        func {function} -- a function that takes a single number
        vec {list} -- vector

    Returns:
        list -- vector
    """
    result = vec[:]
    for i in range(len(vec)):
        result[i] = func(vec[i])
    return result
