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
    pass

def transpose(matrix):
    pass

############################################################
# Section 3: Sequence Slicing
############################################################

def copy(seq):
    pass

def all_but_last(seq):
    pass

def every_other(seq):
    pass

############################################################
# Section 4: Combinatorial Algorithms
############################################################

def prefixes(seq):
    pass

def suffixes(seq):
    pass

def slices(seq):
    pass

############################################################
# Section 5: Text Processing
############################################################

def normalize(text):
    pass

def no_vowels(text):
    pass

def digits_to_words(text):
    pass

def to_mixed_case(name):
    pass

############################################################
# Section 6: Polynomials
############################################################

class Polynomial(object):

    def __init__(self, polynomial):
        pass

    def get_polynomial(self):
        pass

    def __neg__(self):
        pass

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __call__(self, x):
        pass

    def simplify(self):
        pass

    def __str__(self):
        pass

############################################################
# Section 7: Feedback
############################################################

feedback_question_1 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""

feedback_question_2 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""

feedback_question_3 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""
