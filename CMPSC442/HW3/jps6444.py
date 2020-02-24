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
import math


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
        if self.is_solved():
            return []
        class PuzzleQueue():
            def __init__(self, heur, puzzle, moves):
                self.heur = heur
                self.puzzle = puzzle
                self.moves = moves
            
            def __lt__(self, other):
                return (self.heur + len(self.moves)) <= (other.heur + len(other.get_moves()))
            
            def get_puzzle(self):
                return self.puzzle
            
            def get_moves(self):
                return self.moves
                
        # A star with manhattan distance heurtistic
        frontier = queue.PriorityQueue() # Priority queue
        frontier.put(PuzzleQueue(0, self, []))
        explored = {} # graph search must track explored board states
        # here explored means expanded or in frontier

        while not frontier.empty():
            # Get front of queue
            expand_object = frontier.get()
            expand_state = expand_object.get_puzzle()
            expand_move = expand_object.get_moves()

            # expand node
            next_level = expand_state.successors()
            for move, new_puzzle in next_level:
                new_moves = expand_move[:]
                new_moves.append(move)
                # check if explored already
                board = new_puzzle.get_board()
                board_tuple = tuple(map(tuple, board))
                if board_tuple in explored.keys():
                    # check if new move list is better
                    if len(new_moves) > len(explored[board_tuple]):
                        continue # state already found

                # check if solution
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
                # add new state to frontier
                explored[board_tuple] = new_moves
                frontier.put(PuzzleQueue(heur, new_puzzle, new_moves))

############################################################
# Section 2: Grid Navigation
############################################################

def find_path(start, goal, scene):
    """Finds a solutions from start to goal using an A* seach
    with Euclidean distance heuristic.
    
    Arguments:
        start {tuple(int, int)} -- Start point (row, column)
        goal {tuple(int, int)} -- Goal  point (row, column)
        scene {list[list]} -- 2D list of booleans (true = obstacle)
    
    Returns:
        list[tuple] -- Move list of optimal solution (move is new spot)
    """
    if start == goal:
        return start
    elif scene[start[0]][start[1]] or scene[goal[0]][goal[1]]:
        return None # start or goal on obstacle
    class SceneQueue():
        def __init__(self, heur, moves):
            self.heur = heur
            self.moves = moves
        
        def __lt__(self, other):
            return (self.heur + len(self.moves)) <= (other.heur + len(other.get_moves()))
        
        def get_moves(self):
            return self.moves
            
    # A star with euclidean distance heurtistic
    frontier = queue.PriorityQueue() # Priority queue
    frontier.put(SceneQueue(0, [start]))
    explored = set()
    # here explored means expanded or in frontier

    while not frontier.empty():
        # Get front of queue
        expand_object = frontier.get()
        expand_move = expand_object.get_moves()
        current_point = expand_move[len(expand_move) - 1] # last point is current

        # expand node
        next_level = grid_successors(current_point, scene)

        for next_point in next_level:
            new_moves = expand_move[:]
            new_moves.append(next_point)

            if next_point in explored:
                continue

            # check if solution
            if next_point == goal:
                return new_moves

            # calculate heuristic
            cur_row = next_point[0]
            cur_col = next_point[1]

            goal_row = goal[0]
            goal_col = goal[1]

            heur = math.sqrt((goal_row - cur_row)**2 + (goal_col - cur_col)**2)

            # add new move_list to frontier
            frontier.put(SceneQueue(heur, new_moves))
            explored.add(next_point)

    return None

def grid_successors(point, scene):
    cur_row = point[0]
    cur_col = point[1]
    if cur_row > 0: # can go up
        if scene[cur_row - 1][cur_col] != True:
            yield (cur_row - 1, cur_col)
        if cur_col > 0: # can go up/left
            if scene[cur_row - 1][cur_col - 1] != True:
                yield (cur_row - 1, cur_col - 1)
        if cur_col < (len(scene[0])-1): # can go up/right
            if scene[cur_row - 1][cur_col + 1] != True:
                yield (cur_row - 1, cur_col + 1)
    if cur_row < (len(scene) - 1): # can go down
        if scene[cur_row + 1][cur_col] != True:
            yield (cur_row + 1, cur_col)
        if cur_col > 0: # can go down/left
            if scene[cur_row + 1][cur_col - 1] != True:
                yield (cur_row + 1, cur_col - 1)
        if cur_col < (len(scene[0])-1): # can go down/right
            if scene[cur_row + 1][cur_col + 1] != True:
                yield (cur_row + 1, cur_col + 1)
    if cur_col < (len(scene[0]) - 1): # go right
        if scene[cur_row][cur_col + 1] != True:
            yield (cur_row, cur_col + 1)
    if cur_col > 0: # go left
        if scene[cur_row][cur_col - 1] != True:
            yield (cur_row, cur_col - 1)

############################################################
# Section 3: Linear Disk Movement, Revisited
############################################################

def solve_distinct_disks(length, n):
    """Finds a solution to the disks puzzle such that the list of
    (from, to) moves results in a valid states. Uses A* search
    with heuristics that calculates total out of position values.

    :return solution: a list of (from, to) tuple pairs that lead to a solution
    """
    # ADD IN FIRST CHECKS
    class DiskQueue():
        def __init__(self, heur, state ,moves):
            self.heur = heur
            self.state = state
            self.moves = moves
        
        def __lt__(self, other):
            return (self.heur + len(self.moves)) <= (other.heur + len(other.get_moves()))
        
        def get_state(self):
            return self.state

        def get_moves(self):
            return self.moves
            
    # A star with euclidean distance heurtistic
    frontier = queue.PriorityQueue() # Priority queue
    frontier.put(DiskQueue(0, create_disk_puzzle(length, n), []))
    explored = {} # graph search must track explored board states
    # here explored means expanded or in frontier

    while not frontier.empty():
        # Get front of queue
        expand_object = frontier.get()
        expand_state = expand_object.get_state()
        expand_move = expand_object.get_moves()

        # expand node
        next_level = expand_disk_puzzle(expand_state)
        for move, new_puzzle in next_level:
            new_moves = expand_move[:]
            new_moves.append(move)
            # check if explored already
            board_tuple = tuple(new_puzzle)
            if board_tuple in explored.keys():
                # check if new move list is better
                if len(new_moves) > len(explored[board_tuple]):
                    continue # state already found

            # check if solution
            if disk_puzzle_solved(new_puzzle, n):
                return new_moves

            # calculate heuristic
            heur = 0
            for i in range(n):
                current_ind = new_puzzle.index(i+1)
                goal_ind = length - (i+1)
                heur += abs(current_ind - goal_ind)

            # add new state to frontier
            explored[board_tuple] = new_moves
            frontier.put(DiskQueue(heur, new_puzzle, new_moves))
    return None

def create_disk_puzzle(length, n):
    """Creates a list to represent a linear disk puzzle.
    The list will be of size length and contain n disks.

    :param length: size of puzzle
    :param n: number of disks in puzzle

    :return puzzle: list of binary values
    """
    return [i + 1 if i < n else 0 for i in range(length)] # index + 1 for distinct


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
            yield ((i, i - 1), new_puzzle)
        elif (i - 2) >= 0 and puzzle[i - 2] == 0:
            # can jump
            new_puzzle[i - 2] = new_puzzle[i]
            new_puzzle[i] = 0
            yield ((i, i - 2), new_puzzle)

def disk_puzzle_solved(puzzle, n):
    """Checks to see if disk puzzle has been solved.

    :param puzzle: puzzle state to check
    :param distinct: boolean that determines goal state to check for

    :return is_solved: true if puzzle is solved; false otherwise
    """
    length = len(puzzle)
    # order in distinct matters
    return puzzle[(length - n):length] == [n - i for i in range(n)]
    

############################################################
# Section 4: Dominoes Game
############################################################

def create_dominoes_game(rows, cols):
    board = [[False for j in range(cols)] for i in range(rows)]
    return DominoesGame(board)

class DominoesGame(object):

    # Required
    def __init__(self, board):
        self.board = board
        self.m = len(board) # row
        self.n = len(board[0]) # col

    def get_board(self):
        return self.board

    def reset(self):
        self.board = [[False for j in range(self.n)] for i in range(self.m)]

    def is_legal_move(self, row, col, vertical):
        if row == self.m - 1 and vertical:
            return False
        if col == self.n - 1 and not vertical:
            return False
        if self.board[row][col] == True:
            return False
        elif self.board[row][col + 1] == True and not vertical:
            return False
        elif self.board[row + 1][col] == True and vertical:
            return False
        return True

    def legal_moves(self, vertical):
        for i in range(self.m):
            for j in range(self.n):
                if self.is_legal_move(i, j, vertical):
                    yield((i, j))

    def perform_move(self, row, col, vertical):
        if self.is_legal_move(row, col, vertical):
            self.board[row][col] = True
            if vertical:
                self.board[row + 1][col] = True
            else:
                self.board[row][col + 1] = True

    def game_over(self, vertical):
        if len(self.legal_moves(vertical)) == 0:
            return True
        return False

    def copy(self):
        new_board = []
        for i in range(self.m):
            new_board.append(self.board[i][:])
        return DominoesGame(new_board)

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
