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

class BayesNet1 :
    def __init__ ( self , seed , k =10) :
        prng = np . random . RandomState ( seed )
        prob_a = frac ( prng . randint (1 , 2** k ) , 2** k ) # P ( a =1)
        prob_b = {(1 ,) : frac ( prng . randint (1 , 2** k ) , 2** k ) , # P ( b =1 | a =1)
                (0 ,) : frac ( prng . randint (1 , 2** k ) , 2** k ) # P ( b =1 | a =0)
                }
        prob_c = {(1 ,) : frac ( prng . randint (1 , 2** k ) , 2** k ) , # P ( c =1 | a =1)
                (0 ,) : frac ( prng . randint (1 , 2** k ) , 2** k ) # P ( c =1 | a =0)
                }
        prob_d = {(0 , 0) : frac ( prng . randint (1 , 2** k ) , 2** k ) , # P ( d =1 | b =0 ,
                (0 , 1) : frac ( prng . randint (1 , 2** k ) , 2** k ) , # P ( d =1 | b =0 ,
                (1 , 0) : frac ( prng . randint (1 , 2** k ) , 2** k ) , # P ( d =1 | b =1 ,
                (1 , 1) : frac ( prng . randint (1 , 2** k ) , 2** k ) , # P ( d =1 | b =1 ,
                }
        def a ( value ) : # returns P ( a = value )
            if value == 1:
                return prob_a
            else :
                return 1 - prob_a

        def b ( value , a ) : # returns P ( b = value | a )
            tmp = prob_b [( a ,) ]
            if value == 1:
                return tmp
            else :
                return 1 - tmp

        def c ( value , a ) : # returns P ( c = value | a )
            tmp = prob_c [( a ,) ]
            if value == 1:
                return tmp
            else :
                return 1 - tmp

        def d ( value , b , c ) : # returns P ( d = value | b , c )
            tmp = prob_d [( b , c ) ]
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