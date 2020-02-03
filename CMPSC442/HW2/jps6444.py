############################################################
# CMPSC 442: Homework 2
############################################################

student_name = "Joseph Sepich"

############################################################
# Imports
############################################################

# Include your imports here, if any are used.
import math


############################################################
# Section 1: N-Queens
############################################################

def num_placements_all(n):
    """Calculates the number of possible ways to place n
    queens on an n x n chessboard.

    :param n: number of queens/size of board

    :return combinations: number of possible arrangements
    """
    # one in row x of n * one in row x of n ...
    # n ^ n
    return n ** n

def num_placements_one_per_row(n):
    """Calculates the number of possible ways to place n
    queens on an n x n chessboard with only one per row.

    :param n: number of queens/size of board

    :return permutations: number of possible arrangements
    """
    # one in row x of n * one in row x of n-1 ...
    # n!
    return math.factorial(n)

def n_queens_valid(board):
    pass

def n_queens_solutions(n):
    pass

############################################################
# Section 2: Lights Out
############################################################

class LightsOutPuzzle(object):

    def __init__(self, board):
        pass

    def get_board(self):
        pass

    def perform_move(self, row, col):
        pass

    def scramble(self):
        pass

    def is_solved(self):
        pass

    def copy(self):
        pass

    def successors(self):
        pass

    def find_solution(self):
        pass

def create_puzzle(rows, cols):
    pass

############################################################
# Section 3: Linear Disk Movement
############################################################

def solve_identical_disks(length, n):
    pass

def solve_distinct_disks(length, n):
    pass

############################################################
# Section 4: Feedback
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
