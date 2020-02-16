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
        self.assertEqual(hw.question_matmat(mat, vec), [[6, 12, 18, 24]])
        vec = [[1, 3], [1, 3], [1, 3], [1, 3], [2, 3]]
        self.assertEqual(hw.question_matmat(mat, vec), [[6, 12, 18, 24], [15, 30, 45, 60]])


if __name__ == '__main__':
    unittest.main()