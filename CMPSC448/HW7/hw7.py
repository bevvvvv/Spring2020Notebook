"""
CMPSC448 Machine Learning and AI Homework 7
Bayesian Networks
Author: Joseph Sepich (jps6444)
Due April 27
"""
# import statements
from fractions import Fraction as frac

# constants

def question1Part1():
    pathverdict = [
        (('a', 'b', 'd',), True) # HT blockage
        (('a', 'e', 'd'), True) # HH blockage
    ]
    result = True
    return result, pathverdict

def question1Part2():
    pathverdict = [
        (('a', 'b', 'd', 'c', 'g'), False) # none
        (('a', 'b', 'e', 'f', 'g'), True) # HT blockage
        (('a', 'e', 'f', 'g'), True) # HT blockage
    ]
    result = False
    return result, pathverdict

def question1Part3():
    pathverdict = [
        (('a', 'b', 'd', 'c', 'g'), False) # none
        (('a', 'b', 'e', 'f', 'g'), True) # HT blockage
        (('a', 'e', 'f', 'g'), True) # HT blockage
    ]
    result = False
    return result, pathverdict

def question1Part4():
    pathverdict = [
        (('a', 'b', 'd', 'c', 'g'), True) # HT blockage
        (('a', 'b', 'e', 'f', 'g'), True) # HT blockage
        (('a', 'e', 'f', 'g'), False) # none
    ]
    result = False
    return result, pathverdict

def question2Part1():
    pathverdict = [
        (('a', 'b', 'c', 'd'), True) # HH blockage
        (('a', 'b', 'e', 'f', 'g', 'd'), True) # HT blockage
    ]
    result = True
    return result, pathverdict

def question2Part2():
    pathverdict = [
        (('a', 'b', 'c', 'd'), False) # none
        (('a', 'b', 'e', 'f', 'g', 'd'), True) # TT blockage
    ]
    result = False
    return result, pathverdict

def question2Part3():
    pathverdict = [
        (('b', 'c', 'd', 'g'), True) # TT blockage
        (('b', 'e', 'f', 'g'), True) # HT blockage
    ]
    result = True
    return result, pathverdict

def question3Part1(a,b,c,d, bn):
  pass
def question3Part2(a,b,c, bn):
  pass
def question3Part3(d, bn):
  pass
def question3Part4(a,b,c, bn):
  pass
def question3Part4(c, d, bn):
  pass
def question4Part1(b,c,d, bn):
  pass
def question4Part2(c, d, bn):
  pass
def question4Part3(d, e, bn):
  pass
