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
        diff = abs(hw.question1(10) - 0.8267)
        self.assertLess(diff, 0.000464)
        # Almost correct. Expected: 0.8267 +/- 0.000464, got:0.8274999999999946. Input: num_models = 10

    def test_question2(self):
        (a, b, c) = hw.question2(10)
        diff = abs(a - 0.2448069)
        diff = abs(b - 0.1399243)
        diff = abs(c - 0.6152688)
        self.assertLess(diff, 0.00129)
        self.assertLess(diff, 0.00278)
        self.assertLess(diff, 0.00146)
        # Correct. Expected: [0.2448069, 0.1399243, 0.6152688] +/- [0.00129, 0.00278, 0.00146], got: (0.244968, 0.14025, 0.614782) Input: num_models = 10

    def test_question3(self):
        results = np.array([[0, 1],[0, 1],[0, 1],[0, 1],[0, 1],[0, 1],[0, 1]])
        self.assertAlmostEqual(hw.question3(results), 1.0)
        results = np.array([[0, 0],[1, 1],[0, 1],[1, 0],[1, 1],[1, 1],[0, 1]])
        self.assertAlmostEqual(hw.question3(results), 1.0)
        # Correct. Expected: 0.8331021 +/- 0.00111, got: 0.83235

if __name__ == '__main__':
    unittest.main()
