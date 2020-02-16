"""
CMPSC448 Machine Learning and AI Homework 4a Testing
Matrices From Scratch
Author: Joseph Sepich (jps6444)
"""
import unittest
import HW4.hw4a as hw
import numpy as np

class TestHWQuestions(unittest.TestCase):
    def test_matvec(self):
        vec = [1, 1, 1, 1]
        mat = [[1, 1, 1, 1, 1],[2, 2, 2, 2, 2],[3, 3, 3, 3, 3]]
        dim_except = Exception('Dimension Mistmatch')
        with self.assertRaisesRegex(Exception, 'Dimension Mismatch'):
            hw.question_matvec(mat, vec)
        mat.append([4, 4, 4, 4, 4])
        with self.assertRaisesRegex(Exception, 'Dimension Mismatch'):
            hw.question_matvec(mat, vec)
        vec.append(2)
        self.assertEqual(hw.question_matvec(mat, vec), [6, 12, 18, 24])

    def test_matmat(self):
        vec =  [[1], [1], [1], [1]]
        mat = [[1, 1, 1, 1, 1],[2, 2, 2, 2, 2],[3, 3, 3, 3, 3]]
        dim_except = Exception('Dimension Mistmatch')
        with self.assertRaisesRegex(Exception, 'Dimension Mismatch'):
            hw.question_matmat(mat, vec)
        mat.append([4, 4, 4, 4, 4])
        with self.assertRaisesRegex(Exception, 'Dimension Mismatch'):
            hw.question_matmat(mat, vec)
        vec = [[1], [1], [1], [1], [2]]
        self.assertEqual(hw.question_matmat(mat, vec), [[6], [12], [18], [24]])
        vec = [[1, 3], [1, 3], [1, 3], [1, 3], [2, 3]]
        self.assertEqual(hw.question_matmat(mat, vec), [[6, 15], [12, 30], [18, 45], [24, 60]])

    def test_matrixaddition(self):
        x = [[1, 1, 1, 1],[2, 2, 2, 2],[3,3,3,3],[4,4,4,4]]
        b = [[1, 1, 1, 1],[2, 2, 2, 2],[3,3,3,3],[4,4,4,4]]
        self.assertEqual(hw.matrix_addition(x, b),
        [[2, 2, 2, 2],[4, 4, 4, 4],[6,6,6,6],[8,8,8,8]])
        x = [[1, 1, 1, 1],[2, 2, 2, 2],[3,3,3,3],[4,4,4,4]]
        self.assertEqual(hw.matrix_addition(x, b, True),
        [[0, 0, 0, 0],[0, 0, 0, 0],[0,0,0,0],[0,0,0,0]])

    def test_vectoraddition(self):
        x = [1, 2, 3, 4]
        b = [1, 2, 3, 4]
        self.assertEqual(hw.vector_addition(x, b), [2, 4, 6, 8])
        self.assertEqual(hw.vector_addition(x, b, True), [0, 0, 0, 0])

    def test_transpose(self):
        A = [[1, 2, 3],
            [4, 5, 6]]
        self.assertEqual(hw.transpose(A), [[1, 4], [2, 5], [3, 6]])

    def test_question3(self):
        A = [[1.2, 1.4, 1], [2, 1.5, 4]]
        W = [[1.2, 1], [1, 1.6]]
        x = [1, 1.4, 1.5] 
        b = [1, 1]
        self.assertEqual(hw.question3(A, W, x, b), [105.2608, 92.4376, 172.744])

    def test_question4(self):
        A = [[1, 3, 2.5], [0, 1, 2.125]]
        C = [[4, 7, 1.5], [1, 2, 1.125]]
        W = [[1, 1], [1.125, 1.5]]
        x = [1, 5, 1]
        b = [4, 2]
        d = [3, 5]
        self.assertEqual(hw.question4(A, C, W, x, b, d), [147.875, 372.984375, 279.28125 ])

    def test_question5(self):
        A = [[4, 1, 6, 8], [2, 5, 1, 0], [1, 2, 1, 5]]
        x = [9, 0, 8, 5]
        self.assertEqual(hw.question5(A, x, sigmoid),0)

    def test_question6(self):
        pass

    def test_question7(self):
        pass

    def test_question8(self):
            pass

def sigmoid(x):
    result = 1.0/(1 + np.exp(-np.array(x)))
    return result.tolist()

def huber(x):
    myval = np.array(x)
    result = np.where(np.abs(myval) <= 1, 0.5*myval**2, np.abs(myval)-0.5)
    return result.sum()

if __name__ == '__main__':
    unittest.main()