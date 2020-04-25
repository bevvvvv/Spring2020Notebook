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
        (('a', 'b', 'd',), True), # HT blockage
        (('a', 'e', 'd'), False), # none
        (('a', 'e', 'f', 'g', 'c', 'd'), False) # none
    ]
    result = False
    return result, pathverdict

def question1Part2():
    pathverdict = [
        (('a', 'b', 'd', 'c', 'g'), False), # none
        (('a', 'b', 'e', 'f', 'g'), True), # HT blockage
        (('a', 'e', 'f', 'g'), True) # HT blockage
    ]
    result = False
    return result, pathverdict

def question1Part3():
    pathverdict = [
        (('a', 'b', 'd', 'c', 'g'), False), # none
        (('a', 'b', 'e', 'f', 'g'), True), # HT blockage
        (('a', 'e', 'f', 'g'), True) # HT blockage
    ]
    result = False
    return result, pathverdict

def question1Part4():
    pathverdict = [
        (('a', 'b', 'd', 'c', 'g'), True), # HT blockage
        (('a', 'b', 'e', 'f', 'g'), True), # HT blockage
        (('a', 'e', 'f', 'g'), False) # none
    ]
    result = False
    return result, pathverdict

def question2Part1():
    pathverdict = [
        (('a', 'b', 'c', 'd'), True), # HH blockage
        (('a', 'b', 'e', 'f', 'g', 'd'), True) # HT blockage
    ]
    result = True
    return result, pathverdict

def question2Part2():
    pathverdict = [
        (('a', 'b', 'c', 'd'), False), # none
        (('a', 'b', 'e', 'f', 'g', 'd'), True) # TT blockage
    ]
    result = False
    return result, pathverdict

def question2Part3():
    pathverdict = [
        (('b', 'c', 'd', 'g'), True), # TT blockage
        (('b', 'e', 'f', 'g'), True) # HT blockage
    ]
    result = True
    return result, pathverdict

def question3Part1(a,b,c,d, bn):
    p_a = bn.a(value=a)
    p_b = bn.b(value=b)
    p_c = bn.c(value=c, a=a, b=b)
    p_d = bn.d(value=d, c=c)

    return p_a * p_b * p_c * p_d

def question3Part2(a,b,c, bn):
    p_a = bn.a(value=a)
    p_b = bn.b(value=b)
    p_c = bn.c(value=c, a=a, b=b)

    return p_a * p_b * p_c

def question3Part3(d, bn):
    a_vals = [i for i in range(2)]
    b_vals = [i for i in range(2)]
    c_vals = [i for i in range(2)]

    return sum([question3Part1(a, b, c, d, bn) for a in a_vals for b in b_vals for c in c_vals])

def question3Part4(a,b,c, bn):
    numerator = question3Part2(a, b, c, bn)
    denonm = sum([question3Part2(i, j, c, bn) for i in range(2) for j in range(2)]) # p(c)

    return numerator / denonm

def question3Part5(c, d, bn):
    numerator = bn.d(value=d, c=c) * sum([question3Part2(i, j, c, bn) for i in range(2) for j in range(2)])
    denom = question3Part3(d, bn)

    return numerator / denom

def question4Part1(b,c,d, bn):
    p_d = bn.d(value=d, b=b, c=c)

    return sum([bn.a(value=a) * bn.b(value=b, a=a) * bn.c(value=c, a=a) * p_d for a in range(2)])

def question4Part2(c, d, bn):
    return sum([bn.d(value=d, b=b, c=c) * bn.b(value=b, a=a) for b in range(2) for a in range(2)])

def question4Part3(d, e, bn):
    p_ed = bn.e(value=e, d=d)
    numerator = p_ed * sum([bn.d(value=d, b=b, c=c) * bn.b(value=b, a=a) * bn.c(value=c, a=a) * bn.a(value=a) for a in range(2) for b in range(2) for c in range(2)])
    denom = sum([bn.e(value=e, d=d) * bn.d(value=d, b=b, c=c) * bn.b(value=b, a=a) * bn.c(value=c, a=a) * bn.a(value=a) for a in range(2) for b in range(2) for c in range(2)])

    return numerator / denom
