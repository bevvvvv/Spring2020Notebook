"""
CMPSC448 Machine Learning and AI Homework 3
Randomization
Author: Joseph Sepich (jps6444)

TESTING SCRIPT
"""
import matplotlib.pyplot as plt
import HW3.hw3 as hw

STEP = 100
MAX = 10100

accuracy = []
iterations = []

plt.plot(iterations, accuracy)

for i in range(STEP, MAX, STEP):
    accuracy.append(hw.question1(20, i))
    iterations.append(i)
    plt.plot(iterations, accuracy)
    plt.pause(0.01)
