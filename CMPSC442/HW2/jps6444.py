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
        """Generator that will yield all possible successors of the current
        Lights Out game board.

        :return (move, new_puzzle): a tuple with move as a (row, col) tuple representing
        the light toggled and new_puzzle a 2D boolean array of the new game board
        """
        for row in range(self.m):
            for col in range(self.n):
                move = (row, col)
                new_puzzle = self.copy()
                new_puzzle.perform_move(row, col)
                new_puzzle = new_puzzle.get_board()
                yield (move, new_puzzle)

    def find_solution(self):
        """Finds a solution to the Lights Out Puzzle such that the list of
        (row, col) moves results in a 2D list of False boolean values or all
        lights are off. Uses breadth-first graph search.

        :return solution: a list of (row, col) tuple pairs that lead to a solution
        """
        moves_frontier = [[]] # match move sequences to states
        frontier = [self.get_board()] # FIFO queue
        explored = [] # graph search must track explored board states
        # here explored means expanded or in frontier

        while len(frontier) > 0:
            expand_state = frontier.pop(0)
            expand_move = moves_frontier.pop(0)
            next_level = LightsOutPuzzle(expand_state).successors()
            for move, board in next_level:
                # check if solution
                new_moves = expand_move[:]
                new_moves.append(move)
                if LightsOutPuzzle(board).is_solved():
                    return new_moves
                board_tuple = tuple(map(tuple, board))
                if board_tuple in explored or board_tuple in frontier:
                    continue # state already found
                # store move
                moves_frontier.append(new_moves)
                # add new state to frontier
                explored.append(board_tuple)
                frontier.append(board)
        return None



def create_puzzle(rows, cols):
    b = [[False for c in range(cols)] for r in range(rows)]
    return LightsOutPuzzle(b)

############################################################
# Section 3: Linear Disk Movement
############################################################
# Data structure for linear disk puzzle will be a single list
# The list will contain 0 for empty spaces and 1 for spaces
# that contain a disk. The size of this list is L

def create_disk_puzzle(length, n, distinct=False):
    """Creates a list to represent a linear disk puzzle.
    The list will be of size length and contain n disks.

    :param length: size of puzzle
    :param n: number of disks in puzzle

    :return puzzle: list of binary values
    """
    if distinct:
        return [i + 1 if i < n else 0 for i in range(length)] # index + 1 for distinct
    return [1 if i < n else 0 for i in range(length)]

def expand_disk_puzzle(puzzle):
    """Generator that will yield all possible successors of the current
    disk puzzle list.

    :return (move, new_puzzle): a tuple with move as a (from, to) tuple representing
    the disk moved and new_puzzle a list of the new puzzle
    """
    for i in range(len(puzzle)):
        new_puzzle = puzzle[:]
        if puzzle[i] == 0:
            continue
        if (i + 1) < len(puzzle) and puzzle[i + 1] == 0:
            # adjacent space open
            new_puzzle[i + 1] = new_puzzle[i]
            new_puzzle[i] = 0
            yield ((i, i + 1), new_puzzle)
        elif (i + 2) < len(puzzle) and puzzle[i + 2] == 0:
            # can jump
            new_puzzle[i + 2] = new_puzzle[i]
            new_puzzle[i] = 0
            yield ((i, i + 2), new_puzzle)
        elif (i - 1) >= 0 and puzzle[i - 1] == 0:
            # adjacent space open
            new_puzzle[i - 1] = new_puzzle[i]
            new_puzzle[i] = 0
            yield ((i - 1, i), new_puzzle)
        elif (i - 2) >= 0 and puzzle[i - 2] == 0:
            # can jump
            new_puzzle[i - 2] = new_puzzle[i]
            new_puzzle[i] = 0
            yield ((i - 2, i), new_puzzle)

def disk_puzzle_solved(puzzle, n, distinct=False):
    """Checks to see if disk puzzle has been solved.

    :param puzzle: puzzle state to check
    :param distinct: boolean that determines goal state to check for

    :return is_solved: true if puzzle is solved; false otherwise
    """
    length = len(puzzle)
    if distinct:
        # order in distinct matters
        return puzzle[(length - n):length] == [n - i for i in range(n)]
    # checks to see disks are in last n spots
    return sum(puzzle[(length - n):length]) == n

def solve_identical_disks(length, n):
    """Solves identical disk puzzle

    :param length: length of puzzle
    :param n: number of disks

    :return solution: moves to get to solution (from, to) pairs
    """
    return solve_disks(length, n, distinct=False)

def solve_distinct_disks(length, n):
    """Solves distinct disk puzzle

    :param length: length of puzzle
    :param n: number of disks

    :return solution: moves to get to solution (from, to) pairs
    """
    return solve_disks(length, n, distinct=True)

def solve_disks(length, n, distinct=False):
    """Finds a solution to the disks puzzle such that the list of
    (from, to) moves results in a valid states.
    Uses breadth-first graph search, just like Lights Out Puzzle.

    :return solution: a list of (from, to) tuple pairs that lead to a solution
    """
    moves_frontier = [[]] # match move sequences to states
    frontier = [create_disk_puzzle(length, n, distinct)] # FIFO queue
    explored = [] # graph search must track explored board states
    # here explored means expanded or in frontier

    while len(frontier) > 0:
        expand_state = frontier.pop(0)
        expand_move = moves_frontier.pop(0)
        next_level = expand_disk_puzzle(expand_state)
        for move, puzzle in next_level:
            # check if solution
            new_moves = expand_move[:]
            new_moves.append(move)
            if disk_puzzle_solved(puzzle, n, distinct):
                return new_moves
            puzzle_tuple = tuple(puzzle)
            if puzzle_tuple in explored or puzzle_tuple in frontier:
                continue # state already found
            # store move
            moves_frontier.append(new_moves)
            # add new state to frontier
            explored.append(puzzle_tuple)
            frontier.append(puzzle)
    return None

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
