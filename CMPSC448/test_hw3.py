"""
CMPSC448 Machine Learning and AI Homework 3
Randomization
Author: Joseph Sepich (jps6444)

TESTING SCRIPT
"""
import unittest
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

if __name__ == '__main__':
    unittest.main()
