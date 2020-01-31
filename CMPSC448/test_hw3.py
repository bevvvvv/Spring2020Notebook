"""
CMPSC448 Machine Learning and AI Homework 3
Randomization
Author: Joseph Sepich (jps6444)

TESTING SCRIPT
"""
import unittest
import numpy as np
import HW3.hw3 as hw

"""
import matplotlib.pyplot as plt
from statistics import mean

Testing for iteration count
Around 0.870 for 20
ARound 0.6 for 1
ARound 0.77 for 5

STEP = 100
MAX = 10100

accuracy = []
iterations = []

plt.plot(iterations, accuracy)

for i in range(STEP, MAX, STEP):
    accuracy.append(hw.question1(1, i))
    iterations.append(i)
    plt.hlines(mean(accuracy), STEP, MAX)
    plt.plot(iterations, accuracy)
    plt.pause(0.01)
"""

class TestHWQuestions(unittest.TestCase):
    def test_question1(self):
        self.assertAlmostEqual(hw.question1(1), 0.60, 2)
        self.assertAlmostEqual(hw.question1(5), 0.77, 2)
        self.assertAlmostEqual(hw.question1(20), 0.870, 3)

    def test_question2(self):
        (a, b, c) = hw.question2(2)
        self.assertAlmostEqual(a, 0.68, 2)
        self.assertAlmostEqual(b, 0.10, 2)
        self.assertAlmostEqual(c, 0.21, 2)

    def test_question3(self):
        results = np.array([[0, 1],[0, 1],[0, 1],[0, 1],[0, 1],[0, 1],[0, 1]])
        self.assertAlmostEqual(hw.question3(results), 0)

if __name__ == '__main__':
    unittest.main()
