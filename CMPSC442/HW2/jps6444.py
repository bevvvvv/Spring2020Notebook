############################################################
# CMPSC 442: Homework 2
############################################################

student_name = "Joseph Sepich"

############################################################
# Imports
############################################################

# Include your imports here, if any are used.
import math
import random


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
    """Checks whether a board configuration is valid
    meaning no queen can attack another queen.

    :param board: a list a[0...k] where a[i] is the row of the ith queen

    :return is_valid: true if the configuration and false otherwise 
    """
    # queens attack along column - same number
    # queens attack along rows - implicitly valid from data type
    # queens attack along diagonal - difference in row and col are same
    for i in range(len(board)):
        for other in range(i+1, len(board)):
            col_i = board[i]
            col_other = board[other]
            if col_i == col_other:
                return False
            diff_col = abs(col_i - col_other)
            diff_row = abs(i - other)
            if diff_col == diff_row:
                return False
    return True

def n_queens_solutions(n):
    """Finds and yields valid solutions of placing
    n queens on an n by n board.

    :param n: size of board/number of queens

    :return solutions: list of possible solutions in board structure
    """
    # given that board is a list a[1....k]
    # goal state: len(board) == n and n_queens_valid(board) == true
    frontier = [] # LIFO stack, append/pop
    # frontier contains generator for next node
    # check for empty with StopIteration
    frontier.append(n_queens_helper(n, []))
    
    while len(frontier) > 0:
        expand_board = []
        try:
            # get next node
            expand_board = next(frontier[len(frontier) - 1])[:]
        except StopIteration:
            # last generator is done
            frontier.pop()
            continue
        # goal check
        if len(expand_board) == n:
            yield expand_board # only valid options in stack from helper
        # add next level
        frontier.append(n_queens_helper(n, expand_board))

def n_queens_helper(n, board):
    """Generator function for valid solutions of adding
    one additional queen to an n by n chess board.

    :param n: size of board/number of queens
    :param board: a list a[0...k] where a[i] is the row of the ith queen

    :return valid: valid is a valid solution in the format of the board struct
    """
    for i in range(n):
        # try adding to each column
        # yield if column is valid
        board.append(i)
        if n_queens_valid(board):
            yield board
        board.pop() # reset to original value

############################################################
# Section 2: Lights Out
############################################################

class LightsOutPuzzle(object):

    def __init__(self, board):
        """Initializes the lights out puzzle.

        :param board: board is a 2D array of boolean values determining
        light status
        """
        self.board = board
        self.m = len(board)
        self.n = len(board[0])

    def get_board(self):
        """Returns the state of the Lights Out Puzzle board.

        :return board: 2D array of boolean values
        """
        return self.board

    def perform_move(self, row, col):
        """Performs a move on the light's out puzzle. This will
        toggle the given row and column along with neighbors.

        :param row: row of toggled light
        :param col: column of toggled light
        """
        try:
            self.board[row][col] = not self.board[row][col]
        except:
            return # invalid indices
        # left
        if row > 0:
                self.board[row - 1][col] = not self.board[row - 1][col]
        # right
        if row < (self.m - 1):
                self.board[row + 1][col] = not self.board[row + 1][col]
        # up
        if col > 0:
                self.board[row][col - 1] = not self.board[row][col - 1]
        # down
        if col < (self.n - 1):
                self.board[row][col + 1] = not self.board[row][col + 1]

    def scramble(self):
        """Scrambles the baord of the Lights Out Puzzle
        object. Will perform a move on each space with p = 0.5
        """
        for row in range(self.m):
            for col in range(self.n):
                if random.random() < 0.5:
                    self.perform_move(row, col)

    def is_solved(self):
        """Determines whether the Lights Out Puzzle is solved. Solved
        state is when all lights are off or False

        :return is_solved: returns True if solved; false otherwise 
        """
        for row in range(self.m):
            for col in range(self.n):
                if self.board[row][col] == True:
                    return False
        return True

    def copy(self):
        """Creates and returns a deep copy of the Lights Out board object.

        :return board: LightsOutPuzzle object
        """
        b = [row[:] for row in self.board]
        return LightsOutPuzzle(b)

    def successors(self):
        pass

    def find_solution(self):
        pass

def create_puzzle(rows, cols):
    b = [[False for c in range(cols)] for r in range(rows)]
    return LightsOutPuzzle(b)

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
