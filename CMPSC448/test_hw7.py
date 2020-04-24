"""
CMPSC448 Machine Learning and AI Homework 7 Testing
Bayesian Networks
Author: Joseph Sepich (jps6444)
"""
import unittest
import numpy as np
from fractions import Fraction as frac
import HW7.hw7 as hw7

##############################################################################
################# REQUIRED DATA STRUCTURE ####################################
##############################################################################

class BayesNet3: # Problem 3 hw bayes net
    def __init__ (self, seed, k =10) :
        prng = np.random.RandomState(seed)
        prob_a = frac(prng.randint(1, 2**k), 2**k) # P ( a =1)
        prob_b = frac(prng.randint(1, 2**k), 2**k) # P ( b =1)
        prob_c = {(0, 0): frac(prng.randint(1, 2**k), 2**k), # P ( c =1 | a =0, b =0)
                (0, 1): frac(prng.randint(1, 2**k ), 2**k), # P ( c =1 | a =0, b=1)
                (1, 0): frac(prng.randint(1, 2**k ), 2**k), # P ( c =1 | a =0, b=1)
                (1, 1): frac(prng.randint(1, 2**k ), 2**k) # P ( c =1 | a =0, b=1)
                }
        prob_d = {(0,): frac(prng.randint(1, 2**k), 2**k), # P ( d =1 | c =0)
                (1,): frac(prng.randint(1, 2**k ), 2**k), # P ( d =1 | c =1)
                }
        prob_e = {(0,): frac(prng.randint(1, 2**k), 2**k), # P ( e =1 | c =0)
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
    def test_case(self):
        pass


if __name__ == '__main__':
    unittest.main()