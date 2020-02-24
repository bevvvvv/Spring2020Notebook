############################################################
# CMPSC 442: Homework 3
############################################################

student_name = "Joseph Peter Sepich"

############################################################
# Imports
############################################################

# Include your imports here, if any are used.



############################################################
# Section 1: Tile Puzzle
############################################################

def index_2D(myList, value):
    for i, inner in enumerate(myList):
        if value in inner:
            return (i, inner.index(value))

def create_tile_puzzle(rows, cols):
    board = []
    count = 1
    for i in range(rows):
        row_list = []
        for j in range(cols):
            row_list.append(count)
            count += 1
        board.append(row_list)
    board[(rows-1)][(cols-1)] = 0
    return TilePuzzle(board)

class TilePuzzle(object):
    
    # Required
    def __init__(self, board):
        self.board = board # 2D list
        self.m = len(board) # rows
        self.n = len(board[0]) # cols

    def get_board(self):
        return self.board

    def perform_move(self, direction):
        success = False
        valid_moves = ['up', 'down', 'left', 'right']
        if direction not in valid_moves:
            return success
        # index of zero
        zero_ind = index_2D(self.board, 0)
        zero_row = zero_ind[0]
        zero_col = zero_ind[1]
        if direction == 'up':
            if zero_row <= 0:
                return success
            else:
                self.board[zero_row][zero_col] = self.board[zero_row - 1][zero_col]
                self.board[zero_row - 1][zero_col] = 0
                success = True
                return success
        elif direction == 'down':
            if zero_row >= (self.m - 1):
                return success
            else:
                self.board[zero_row][zero_col] = self.board[zero_row + 1][zero_col]
                self.board[zero_row + 1][zero_col] = 0
                success = True
                return success
        elif direction == 'left':
            if zero_col <= 0:
                return success
            else:
                self.board[zero_row][zero_col] = self.board[zero_row][zero_col - 1]
                self.board[zero_row][zero_col - 1] = 0
                success = True
                return success
        else: # right
            if zero_col >= (self.n - 1):
                return success
            else:
                self.board[zero_row][zero_col] = self.board[zero_row][zero_col + 1]
                self.board[zero_row][zero_col + 1] = 0
                success = True
                return success

    def scramble(self, num_moves):
        pass

    def is_solved(self):
        pass

    def copy(self):
        pass

    def successors(self):
        pass

    # Required
    def find_solutions_iddfs(self):
        pass

    # Required
    def find_solution_a_star(self):
        pass

############################################################
# Section 2: Grid Navigation
############################################################

def find_path(start, goal, scene):
    pass

############################################################
# Section 3: Linear Disk Movement, Revisited
############################################################

def solve_distinct_disks(length, n):
    pass

############################################################
# Section 4: Dominoes Game
############################################################

def create_dominoes_game(rows, cols):
    pass

class DominoesGame(object):

    # Required
    def __init__(self, board):
        pass

    def get_board(self):
        pass

    def reset(self):
        pass

    def is_legal_move(self, row, col, vertical):
        pass

    def legal_moves(self, vertical):
        pass

    def perform_move(self, row, col, vertical):
        pass

    def game_over(self, vertical):
        pass

    def copy(self):
        pass

    def successors(self, vertical):
        pass

    def get_random_move(self, vertical):
        pass

    # Required
    def get_best_move(self, vertical, limit):
        pass

############################################################
# Section 5: Feedback
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
