"""
Machine Learning and AI Final
Joseph Sepich
May 7, 2020
"""

# import
from fractions import Fraction as frac



# For Bayesian Network 1
# Return the result and pathverdict that answers this question:
# is ['B'] conditionally independent of ['D'] given ['C']?
def question1():
    result = True
    pathverdict = [
        (('B', 'C', 'D'), True) # H-T blockage
    ]
    return result, pathverdict


# For Bayesian Network 1
# Return P(A,D,E) 
def question2(A, D, E, bn):
    p_a = bn.A(value = A)
    return sum([p_a * bn.B(value = B) * bn.C(value = C, A = A, B = B) * bn.D(value = D, C = C) * bn.E(value = E, C = C) for B in range(2) for C in range(2)])


# For Bayesian Network 2
# Return the result and pathverdict that answers this question:
# is ['a'] independent of ['b']?
def question3():
    result = True
    pathverdict = [
        (('a', 'c', 'b'), True), # all H-H since Z is empty
        (('a', 'd', 'b'), True),
        (('a', 'c', 'e', 'f', 'd', 'b'), True),
        (('a', 'd', 'f', 'e', 'c', 'b'), True)
    ]
    return result, pathverdict


# For Bayesian Network 2
# Return the result and pathverdict that answers this question:
# is ['d'] conditionally independent of ['m'] given ['e']?
def question4():
    result = False
    pathverdict = [
        (('d', 'f', 'h', 'm'), False),
        (('d', 'a', 'c', 'e', 'f', 'h', 'm'), True),
        (('d', 'b', 'c', 'e', 'f', 'h', 'm'), True)
    ]
    return result, pathverdict


# For Bayesian Network 3
# Return the result and pathverdict that answers this question:
# is ['a'] independent of ['c']?
def question5():
    result = True
    pathverdict = [
        (('a', 'd', 'b', 'e', 'c'), True), # all H-H
        (('a', 'd', 'h', 'n', 'k', 'e', 'c'), True),
        (('a', 'd', 'b', 'e', 'k', 'p', 'm', 'f', 'c'), True),
        (('a', 'd', 'h', 'n', 'k', 'p', 'm', 'f', 'c'), True)
    ]
    return result, pathverdict


# For Bayesian Network 3
# Return the result and pathverdict that answers this question:
# is ['h'] conditionally independent of ['g'] given ['b', 'n']?
def question6():
    result = True
    pathverdict = [
        (('h', 'n', 'k', 'p', 'm', 'g'), True), # HH
        (('h', 'n', 'k', 'e', 'c', 'f', 'm', 'g'), True), # HH
        (('h', 'd', 'b', 'e', 'c', 'f', 'm', 'g'), True), # HT
        (('h', 'd', 'b', 'e', 'k', 'p', 'm', 'g'), True), # HT
    ]
    return result, pathverdict


# For Bayesian Network 4
# Return P(c,d) 
def question7(c, d, bn):
    p_d = bn.d(value = d, c = c)
    return sum([bn.a(value = a) * bn.b(value = b, a = a) * bn.c(value = c, a = a, b = b) * p_d for a in range(2) for b in range(2)])


# For Bayesian Network 4
# Return P(c,d | a) 
def question8(c, d, a, bn):
    p_d = bn.d(value = d, c = c)
    return sum([bn.b(value = b, a = a) * bn.c(value = c, a = a, b = b) * p_d for b in range(2)])


# For Bayesian Network 5
# Return P(a,b,e) 
def question9(a, b, e, bn):
    p_a = bn.a(value = a)
    p_b = bn.b(value = b)
    return sum([p_a * p_b * bn.c(value = c, a = a) * bn.e(value = e, b = b, c = c) for c in range(2)])


# For Bayesian Network 5
# Return P(a,b,e | c,d) 
def question10(a, b, e, c, d, bn):
    numerator = bn.a(value = a) * bn.b(value = b) * bn.c(value = c, a = a) * bn.d(value = d, a = a, b = b) * bn.e(value = e, b = b, c = c)
    denom = sum([bn.a(value = a) * bn.b(value = b) * bn.c(value = c, a = a) * bn.d(value = d, a = a, b = b) for a in range(2) for b in range(2)])
    return numerator / denom
