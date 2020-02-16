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
  
def question3(A,W,x,b):
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

  
def question4(A,C,W,x,b,d):
   # function is (Ax-b)'W(Cx-d))
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
   
def question5(A,x,sigmoid):
   pass
   
def question6(A,x,b,sigmoid):
   pass
   
def question7(A,W,x,b,sigmoid):
   pass
   
def question8(A,W,x,b,sigmoid,huber):
   pass 

def matrix_addition(A, B, subtract=False):
   result = A[:][:]
   for row in range(len(A)):
      for col in range(len(A[0])):
         if subtract:
            result[row][col] = A[row][col] - B[row][col]
         else:
            result[row][col] = A[row][col] + B[row][col]
   return result

def vector_addition(x, b, subtract=False):
   result = x[:]
   for i in range(len(x)):
      if subtract:
         result[i] = x[i] - b[i]
      else:
         result[i] = x[i] + b[i]
   return result

def transpose(A):
   A_prime = []
   for col in range(len(A[0])):
      A_prime.append([])
   new_row = 0
   for col in range(len(A[0])):
      for row in range(len(A)):
         A_prime[new_row].append(A[row][col])
      new_row += 1
   return A_prime