"""
CMPSC448 Machine Learning and AI Homework 4a Testing
Matrices From Scratch
Author: Joseph Sepich (jps6444)
"""
import unittest
import HW4.hw4a as hw

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


if __name__ == '__main__':
    unittest.main()