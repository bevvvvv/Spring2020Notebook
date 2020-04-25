"""
CMPSC448 Machine Learning and AI Homework 7 Testing
Bayesian Networks
Author: Joseph Sepich (jps6444)
"""
import unittest
import numpy as np
from fractions import Fraction as frac
import HW7.hw7 as hw

##############################################################################
################# REQUIRED DATA STRUCTURE ####################################
##############################################################################

class BayesNet3: # Problem 3 hw bayes net
    def __init__ (self, seed, k =10) :
        prng = np.random.RandomState(seed)
        self.prob_a = frac(prng.randint(1, 2**k), 2**k) # P ( a =1)
        self.prob_b = frac(prng.randint(1, 2**k), 2**k) # P ( b =1)
        self.prob_c = {(0, 0): frac(prng.randint(1, 2**k), 2**k), # P ( c =1 | a =0, b =0)
                (0, 1): frac(prng.randint(1, 2**k ), 2**k), # P ( c =1 | a =0, b=1)
                (1, 0): frac(prng.randint(1, 2**k ), 2**k), # P ( c =1 | a =0, b=1)
                (1, 1): frac(prng.randint(1, 2**k ), 2**k) # P ( c =1 | a =0, b=1)
                }
        self.prob_d = {(0,): frac(prng.randint(1, 2**k), 2**k), # P ( d =1 | c =0)
                (1,): frac(prng.randint(1, 2**k ), 2**k), # P ( d =1 | c =1)
                }
        self.prob_e = {(0,): frac(prng.randint(1, 2**k), 2**k), # P ( e =1 | c =0)
                (1,): frac(prng.randint(1, 2**k ), 2**k), # P ( e =1 | c =1)
                }

    def a(self, value): # returns P(a=value)
        if value == 1:
            return self.prob_a
        else:
            return 1 - self.prob_a
    
    def b(self, value): # returns P(b=value)
        if value == 1:
            return self.prob_b
        else:
            return 1 - self.prob_b

    def c(self, value, a, b): # returns P(c=value | a,b)
        tmp = self.prob_c[(a,b)]
        if value == 1:
            return tmp
        else:
            return 1 - tmp

    def d(self, value, c): # returns P(d=value | c)
        tmp = self.prob_d[(c,)]
        if value == 1:
            return tmp
        else:
            return 1 - tmp
    
    def e(self, value, c): # returns P(e=value | c)
        tmp = self.prob_e[(c,)]
        if value == 1:
            return tmp
        else:
            return 1 - tmp


##############################################################################
################# TEST CASES #################################################
##############################################################################

class TestHWQuestions(unittest.TestCase):
    def setUp(self):
        self.bn3 = BayesNet3(3)
        return super().setUp()

    def test_question3Part1(self):
        #self.assertEqual(hw.question3Part1(0, 0, 0, 0, self.bn3), 0)
        pass

    def test_question3Part2(self):
        pass

    def test_question3Part3(self):
        pass

    def test_question3Part4(self):
        pass

    def test_question3Part5(self):
        self.assertEqual(hw.question3Part5(0, 0, self.bn3), 0)


if __name__ == '__main__':
    unittest.main()