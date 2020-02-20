"""
CMPSC448 Machine Learning and AI Homework 4b Testing
Calculus and Optimization from Scratch
Author: Joseph Sepich (jps6444)
"""
import unittest
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import HW4.hw4b as hw

class TestHWQuestions(unittest.TestCase):
    def test_question1_loss(self):
        pass

    def test_question2_grad(self):
        pass
        
    def test_question3_update(self):
        pass
        
    def test_question4_n_updates(self):
        pass
        
    def test_question5_nepochs(self):
        pass
        
    def test_question6_sgd(self):
        pass

if __name__ == '__main__':
    unittest.main()

# this code is just a demonstration of functionality
# make sure your code has no free - standing statements

# we will be using the data returned by this function
# the oldfaithful.csv dataset is in the data directory in
# canvas files

def read_data():
    df = pd.read_csv("oldfaithful.csv", sep ="\s+", header ='infer', index_col=0)
    df.insert (0 , 'bias', 1) # add bias as first column
    df.insert (1 , 'sq', df.EruptionLength.values**2)
    X = df [["bias", "sq", "EruptionLength"]]. values
    y = df.WaitingTime.values
    return X,y

'''
How to read data
X, y = read_data()
'''

# how to shuffle data .
# Make sure you have a data matrix X and target y
def makeshuffler(seed=3):
    prng = np.random.RandomState(seed)
    def shuffle(X, y):
        indices = np.arange(y.size)
        prng.shuffle(indices)
        return X[indices], y[indices]
    return shuffle

'''
How to shuffle
shuffle = makeshuffler()
X, y = shuffle(X, y) # shuffled dataset
'''

def sigmoid(x):
    result = 1.0/(1 + np.exp(-np.array(x)))
    return result.tolist ()

def huber(x):
    myval = np.array(x)
    result = np.where(np.abs(myval) <= 1, 0.5*myval**2 , np.abs(myval)-0.5)
    return result.sum()

'''
Example plot of huber function
z = np.arange(-5, 5, 0.1)
plt.plot(z, [huber(a) for a in z ])
plt.show() # program will wait until you close the graph
'''
