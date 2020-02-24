############################################################
# CMPSC 442: Homework 3
############################################################

student_name = "Joseph Peter Sepich"

############################################################
# Imports
############################################################

# Include your imports here, if any are used.
import random
import queue


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
        self.valid_moves = ['up', 'down', 'left', 'right']

    def get_board(self):
        return self.board

    def perform_move(self, direction):
        success = False
        if direction not in self.valid_moves:
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
        for i in range(num_moves):
            direction = random.choice(self.valid_moves)
            self.perform_move(direction)

    def is_solved(self):
        for i in range((self.m * self.n)):
            value = i
            req_row = (value - 1) // self.m
            req_col = value - (req_row * self.n) - 1
            if self.board[req_row][req_col] != value:
                return False
        if self.board[self.m - 1][self.n - 1] != 0:
            return False
        return True

    def copy(self):
        new_board = []
        for row in range(self.m):
            new_board.append(self.board[row][:])
        return TilePuzzle(new_board)

    def successors(self):
        for move in self.valid_moves:
            new_puzzle = self.copy()
            success = new_puzzle.perform_move(move)
            if success:
                yield (move, new_puzzle)

    # Required
    def find_solutions_iddfs(self):
        # add in zero move check
        if self.is_solved():
            yield []
        else:
            move_limit = 1
            while True:
                solutions = self.iddfs_helper(move_limit)
                slns = list(solutions)
                if slns == []:
                    move_limit += 1
                    continue
                for sln in slns:
                    yield sln

    def iddfs_helper(self, move_limit):
        # stack
        frontier = []
        move_frontier = []
        slns = []

        # initialize
        frontier.append(self.successors())
        move_frontier.append([])

        while len(frontier) > 0:
            expand_puzzle = []
            expand_move = ''
            expand_moves = []
            try:
                # expand end of frontier (all moves)
                expand_move, expand_puzzle = next(frontier[len(frontier) - 1]) # get next node
                expand_moves = move_frontier[len(move_frontier) - 1][:] # get current move list
                expand_moves.append(expand_move) # add new move to current move list
            except:
                frontier.pop()
                move_frontier.pop()
                continue
            # goal check
            solved = expand_puzzle.is_solved()
            if solved:
                yield expand_moves # add move list to solutions
            # add new to frontier if not in goal (if it doesn't pass limit)
            if not solved and len(expand_moves) < move_limit:
                frontier.append(expand_puzzle.successors())
                move_frontier.append(expand_moves)
        return None

    # Required
    def find_solution_a_star(self):
        # A star with manhattan distance heurtistic
        moves_frontier = queue.PriorityQueue() # match move sequences to states
        moves_frontier.put((0, []))
        frontier = queue.PriorityQueue() # Priority queue
        frontier.put((0, self))
        explored = set() # graph search must track explored board states
        # here explored means expanded or in frontier

        while not frontier.empty():
            # Get front of queue
            expand_state = frontier.get()
            expand_state = expand_state[1]
            expand_move = moves_frontier.get()
            expand_move = expand_move[1]

            # expand node
            next_level = expand_state.successors()
            for move, new_puzzle in next_level:
                # check if explored already
                board = new_puzzle.get_board()
                if board in explored:
                    continue # state already found

                # check if solution
                new_moves = expand_move[:]
                new_moves.append(move)
                if new_puzzle.is_solved():
                    return new_moves

                # calculate heuristic
                heur = 0
                for row in range(self.m):
                    for col in range(self.n):
                        value = board[row][col]
                        if value == 0:
                            heur += abs(self.m - row - 1)
                            heur += abs(self.n - col - 1)
                        else:
                            req_row = (value - 1) // self.m
                            req_col = value - (req_row * self.n) - 1
                            heur += abs(req_row - row)
                            heur += abs(req_col - col)
                # store move
                moves_frontier.put((heur, new_moves))
                # add new state to frontier
                explored.add(board)
                frontier.put((heur, new_puzzle))

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
