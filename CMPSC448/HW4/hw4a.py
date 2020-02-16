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
   """[summary]
   
   Arguments:
       mat1 {[type]} -- [description]
       mat2 {[type]} -- [description]
   """
   row_mat1 = len(mat1)
   col_mat1 = len(mat1[0])
   row_mat2 = len(mat2)
   col_mat2 = len(mat2[0])
   if col_mat1 != row_mat2:
      raise Exception('Dimension Mismatch')
   result = []
   for col in range(col_mat2):
      vec = []
      for row in mat2:
         vec.append(row[col])
      result.append(question_matvec(mat1, vec))
   return result
  
def question3(A,W,x,b):
  pass
  
def question4(A,C,W,x,b,d):
   pass
   
def question5(A,x,sigmoid):
   pass
   
def question6(A,x,b,sigmoid):
   pass
   
def question7(A,W,x,b,sigmoid):
   pass
   
def question8(A,W,x,b,sigmoid,huber):
   pass 
