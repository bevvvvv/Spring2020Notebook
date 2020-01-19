############################################################
# CMPSC 442: Homework 1
############################################################

student_name = "Joseph Peter Sepich"

############################################################
# Section 1: Python Concepts
############################################################

python_concepts_question_1 = """
Python is both strongly and dynamically typed. Since python is a strongly
typed language, every object has a fixed type. This is why you cannot use
the + operator on a string and integer togeter: \"Age: \" + 21. The integer in
this case would have to be cast to a string for concatenation. Dynamic typing means
that typing for a variable is determined a run time (when it is assigned). There are
two lines of code: x = 420; x = "april". Python would then make x an integer on the first
assignment and a string on the second assigment. This differs from static typing in that
as soon as x is assigned to an integer then it must remain an integer through its scope.
"""

python_concepts_question_2 = """
The problem for the proposed dictionary is that keys cannot be lists.
An easy solution for this would be to flip the key-value pairs in the example
so that the associated names are the keys for the 2-D points:
points_to_names = {"home": [0, 0], "school": [1, 2], "market": [-1, 1]}.
An interesting concept to note is that the coordinates could be use as keys
if they were tuple types (which are immutable and ordered).
"""

python_concepts_question_3 = """
Of the two concatenation functions given the second function would
be significantly faster for larger inputs. Strings are immutable data types
and the first function has to create a new string object for each element in the
list of the strings. The second function however only requires creating a single
new string object.
"""

############################################################
# Section 2: Working with Lists
############################################################

def extract_and_apply(l, p, f):
    return [f(x) for x in l if p(x)]

def concatenate(seqs):
    return [item for iterator in seqs for item in iterator]

def transpose(matrix):
    return [[matrix[r][c] for r in range(len(matrix))] for c in range(len(matrix[0]))]

############################################################
# Section 3: Sequence Slicing
############################################################

def copy(seq):
    return seq[:]

def all_but_last(seq):
    return seq[0:-1]

def every_other(seq):
    return seq[::2]

############################################################
# Section 4: Combinatorial Algorithms
############################################################

def prefixes(seq):
    stop = 0
    while stop <= len(seq):
        yield seq[0:stop]
        stop += 1

def suffixes(seq):
    start = 0
    while start <= len(seq):
        yield seq[start:len(seq)]
        start += 1

def slices(seq):
    first_point = 0
    second_point = 0
    while first_point <= len(seq):
        while second_point <= len(seq):
            out = seq[first_point:second_point]
            if len(out) > 0:
                yield out
            second_point += 1
        first_point += 1
        second_point = 0

############################################################
# Section 5: Text Processing
############################################################

def normalize(text):
    result = text.split(' ')
    result = [x for x in result if len(x) > 0]
    result = " ".join(result)
    return result.lower()

def no_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = text
    for letter in vowels:
        result = result.replace(letter, '')
    return result

def digits_to_words(text):
    digits = [int(digit) for digit in text if digit.isdigit()]
    english = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
    output = [english[digit] for digit in digits]
    return " ".join(output)

def to_mixed_case(name):
    words = name.split('_')
    words = [word for word in words if len(word) > 0]
    for i in range(len(words)):
        if i == 0:
            words[i] = words[i].lower()
        else:
            words[i] = words[i].lower().capitalize()
    return "".join(words)

############################################################
# Section 6: Polynomials
############################################################

class Polynomial(object):

    def __init__(self, polynomial):
        self.poly_tuple = tuple(polynomial)

    def get_polynomial(self):
        return self.poly_tuple

    def __neg__(self):
        neg = [(-pair[0], pair[1]) for pair in self.poly_tuple]
        return Polynomial(neg)

    def __add__(self, other):
        add = []
        for tup in self.get_polynomial():
            add.append(tup)
        for tup in other.get_polynomial():
            add.append(tup)
        return Polynomial(add)

    def __sub__(self, other):
        neg_other = -other
        return self + neg_other

    def __mul__(self, other):
        mul = [(pair[0] * other_pair[0],pair[1] + other_pair[1]) for pair in self.get_polynomial() \
            for other_pair in other.get_polynomial()]
        return Polynomial(mul)

    def __call__(self, x):
        return sum([pair[0] * x ** pair[1] for pair in self.get_polynomial()])

    def simplify(self):
        coeffs = {}
        for pair in self.get_polynomial():
            key = pair[1]
            value = pair[0]
            if key in coeffs:
                coeffs[key] += value
            else:
                coeffs[key] = value
        delete = []
        for key in coeffs.__iter__():
            if coeffs[key] == 0:
                delete.append(key)
        for key in delete:
            del coeffs[key]
        simp = [(coeffs[key], key) for key in coeffs.__iter__()]
        simp.sort(key = lambda x: x[1], reverse = True)
        if len(simp) == 0:
            simp = [(0, 0)]
        self.poly_tuple = tuple(simp)

    def __str__(self):
        string = ""
        first = True
        for pair in self.get_polynomial():
            coeff = pair[0]
            exp = pair[1]
            if first == True: # First term
                if coeff < 0:
                    string += "-"
                    coeff = coeff * -1
                first = False
            else:
                string += " " # operator
                if coeff < 0:
                    string += "- "
                    coeff = coeff * -1
                else:
                    string += "+ "
            use_coeff = coeff != 1
            if exp == 0:
                string += str(coeff)
            elif exp == 1:
                if use_coeff:
                    string += str(coeff)
                string += "x"
            else:
                if use_coeff:
                    string += str(coeff)
                string += "x^" + str(exp)
        return string

############################################################
# Section 7: Feedback
############################################################

feedback_question_1 = """
I spent approximately three hours on this assignment.
"""

feedback_question_2 = """
I found the polynomial section most challenging, because
I had not read the instructions correctly and I was trying
to put the simplify functionality built into each operator.
Most questions were pretty straightforward from lecture.
"""

feedback_question_3 = """
I liked the variety of topics in the assignment and I
really liked having the test cases. This made writing
unit tests for the program really easy. The variety
also helped to cover all the python features we
learned about in lecture and put them in a real setting.
"""
