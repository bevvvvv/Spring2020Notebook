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
        w = [0.3, 1.2, 1.7]
        indices=[1, 3, 5]
        lamb=0.8
        X, y = read_data()
        self.assertAlmostEqual(hw.question1_loss(w, X, y, indices, lamb, huber), 136.68026640000002, 7)

    def test_question2_grad(self):
        w=[0.125, 0.5, 0.75 ]
        indices=[1, 2, 5]
        lamb=0.001
        X, y = read_data()
        result = hw.question2_grad(w, X, y, indices, lamb, huber)
        self.assertAlmostEqual(result[0], -2.99999724, 7)
        self.assertAlmostEqual(result[1], -22.66056697, 7)
        self.assertAlmostEqual(result[2], -8.01598346, 7)
        
    def test_question3_update(self):
        w=[0.125, 0.5, 0.75]
        indices=[1, 2, 5]
        lamb=0.001
        eta=0.1
        X, y = read_data()
        result = hw.question3_update(w,X,y,indices,lamb,eta,huber)
        self.assertAlmostEqual(result[0], 0.42499972, 7)
        self.assertAlmostEqual(result[1], 2.7660567, 7)
        self.assertAlmostEqual(result[2], 1.55159835, 7)
        
    def test_question4_n_updates(self):
        w=[0.125, 0.5, 0.75 ]
        mbatch=32
        lamb=0.1
        eta=1e-07
        n=10
        X, y = read_data()
        shuffle = makeshuffler()
        result = hw.question4_n_updates(w,X,y,lamb,eta,mbatch,n,huber,shuffle)
        self.assertAlmostEqual(result[0], 0.1250272, 3)
        self.assertAlmostEqual(result[1], 0.50036617, 3)
        self.assertAlmostEqual(result[2], 0.75009485, 3)
        
    def test_question5_nepochs(self):
        w=[0.1, 0.2, 0.8]
        mbatch=10
        lamb=0.2
        eta=1e-07
        nepochs=100
        X, y = read_data()
        shuffle = makeshuffler()
        result = hw.question5_nepochs(w,X,y,lamb,eta,mbatch,nepochs,huber,shuffle)
        self.assertAlmostEqual(result[0], 0.1026996, 7)
        self.assertAlmostEqual(result[1], 0.23634267, 7)
        self.assertAlmostEqual(result[2], 0.80941317, 7)
        
    def test_question6_sgd(self):
        w=[5.0, 1.6, 1.9]
        mbatch=15
        lamb=5
        eta=0.001
        nepochs=150
        epsilon=100
        X, y = read_data()
        shuffle = makeshuffler()
        result = hw.question6_sgd(w,X,y,lamb,eta,mbatch,nepochs,epsilon,shuffle)
        self.assertAlmostEqual(result[0], 1.12756068, 7)
        self.assertAlmostEqual(result[1], 0.36081942, 7)
        self.assertAlmostEqual(result[2], 0.42847306, 7)

if __name__ == '__main__':
    unittest.main()

# this code is just a demonstration of functionality
# make sure your code has no free - standing statements

# we will be using the data returned by this function
# the oldfaithful.csv dataset is in the data directory in
# canvas files

def read_data():
    df = pd.read_csv(r"C:\GitRepos\Spring2020Notebook\CMPSC448\HW4\oldfaithful.csv", sep ="\s+", header ='infer', index_col=0)
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
