# import
import unittest
import HW3.jps6444 as hw

# create test class
class TestHWQuestions(unittest.TestCase):

    # TILE PUZZLE SECTION ONE #
    
    def test_create_tile_puzzle(self):
        """Will test create puzzle, init, and
        get board.
        """
        p = hw.create_tile_puzzle(3, 3)
        self.assertEqual(p.get_board(), [[1,2,3],[4,5,6],[7,8,0]])
        p = hw.create_tile_puzzle(2, 4)
        self.assertEqual(p.get_board(), [[1,2,3,4],[5,6,7,0]])
        p = hw.create_tile_puzzle(1, 4)
        self.assertEqual(p.get_board(), [[1,2,3,0]])

    def test_perform_move(self):
        """Tests a perform move for tile puzzle
        """
        p = hw.create_tile_puzzle(3, 3)
        self.assertFalse(p.perform_move("taco"))
        self.assertTrue(p.perform_move('up'))
        self.assertEqual(p.get_board(), [[1,2,3],[4,5,0],[7,8,6]])
        self.assertFalse(p.perform_move('right'))
        p = hw.create_tile_puzzle(2, 4)
        self.assertTrue(p.perform_move('left'))
        self.assertTrue(p.perform_move('up'))
        self.assertFalse(p.perform_move('up'))
        self.assertEqual(p.get_board(), [[1,2,0,4],[5,6,3,7]])
        p = hw.create_tile_puzzle(1, 4)
        self.assertTrue(p.perform_move('left'))
        self.assertTrue(p.perform_move('left'))
        self.assertTrue(p.perform_move('left'))
        self.assertFalse(p.perform_move('down'))
        self.assertFalse(p.perform_move('left'))
        self.assertEqual(p.get_board(), [[0,1,2,3]])

    def test_is_solved(self):
        """Tests to see if tile game is solved.
        """
        p = hw.TilePuzzle([[1, 2], [3, 0]])
        self.assertTrue(p.is_solved())
        p = hw.TilePuzzle([[0, 1], [3, 2]])
        self.assertFalse(p.is_solved())

    def test_copy(self):
        """Tests tile puzzle copy method.
        """
        p = hw.create_tile_puzzle(3, 3)
        p2 = p.copy()
        self.assertTrue(p.get_board() == p2.get_board())
        p2.perform_move('up')
        self.assertFalse(p.get_board() == p2.get_board())
    
    def test_successors(self):
        """Tests tile puzzle successor method
        """
        p = hw.create_tile_puzzle(3, 3)
        move_results = ['up', 'left']
        board_reuslts = [[[1, 2, 3], [4, 5, 0], [7, 8, 6]], [[1, 2, 3], [4, 5, 6], [7, 0, 8]]]
        i = 0
        for move, new_p in p.successors():
            self.assertEqual(move, move_results[i])
            self.assertEqual(new_p.get_board(), board_reuslts[i])
            i += 1

        p = hw.TilePuzzle([[1,2,3], [4,0,5], [6,7,8]])
        move_results = ['up', 'down', 'left', 'right']
        board_reuslts = [[[1,0,3], [4,2,5], [6,7,8]], [[1,2,3], [4,7,5], [6,0,8]],
                         [[1,2,3], [0,4,5], [6,7,8]], [[1,2,3], [4,5,0], [6,7,8]]]
        i = 0
        for move, new_p in p.successors():
            self.assertEqual(move, move_results[i])
            self.assertEqual(new_p.get_board(), board_reuslts[i])
            i += 1

    def test_find_solutions_iddfs(self):
        b = [[4,1,2], [0,5,3], [7,8,6]]
        p = hw.TilePuzzle(b)
        solutions = p.find_solutions_iddfs()
        results = [['up', 'right', 'right', 'down', 'down']]
        for i in range(len(results)):
            sln = next(solutions)
            self.assertEqual(sln, results[i])

        b = [[1,2,3], [4,0,8], [7,6,5]]
        p = hw.TilePuzzle(b)
        solutions = p.find_solutions_iddfs()
        results = [['down', 'right', 'up', 'left', 'down', 'right'],
                    ['right', 'down', 'left', 'up', 'right', 'down']]
        for i in range(len(results)):
            sln = next(solutions)
            self.assertEqual(sln, results[i])
        # test already solved
        b = [[1,2,3], [4,5,6], [7,8,0]]
        p = hw.TilePuzzle(b)
        solutions = p.find_solutions_iddfs()
        results = []
        for i in range(len(results)):
            sln = next(solutions)
            self.assertEqual(sln, results[i])

    def test_find_solution_a_start(self):
        b = [[4,1,2], [0,5,3], [7,8,6]]
        p = hw.TilePuzzle(b)
        solution = p.find_solution_a_star()
        self.assertEqual(solution, ['up', 'right', 'right', 'down', 'down'])

        b = [[1,2,3], [4,0,5], [6,7,8]]
        p = hw.TilePuzzle(b)
        solution = p.find_solution_a_star()
        self.assertEqual(solution, ['right', 'down', 'left', 'left', 'up', 'right', 'down', 'right', 'up', 'left',
                                    'left', 'down', 'right', 'right'])

        b = [[1,2,3], [4,5,6], [7,8,0]]
        p = hw.TilePuzzle(b)
        solution = p.find_solution_a_star()
        self.assertEqual(solution, [])

    # GRID SEARCH SECTION 2 #
    def test_find_path(self):
        scene = [[False, False, False], [False, True, False], [False, False, False]]
        self.assertEqual(hw.find_path((0,0), (2,1), scene), [(0, 0), (1, 0), (2, 1)])
        scene = [[False, True, False], [False, True, False], [False, True, False]]
        self.assertEqual(hw.find_path((0,0), (0,2), scene), None)
        scene = [[False, False, False], [False, True, False], [False, False, False]]
        self.assertEqual(hw.find_path((1,1), (2,1), scene), None)
        scene = [[False, False, False], [False, True, False], [False, False, False]]
        self.assertEqual(hw.find_path((0,0), (1,1), scene), None)

    # DISTINCT DISKS SECTION 3 #

    def test_solve_distinct_disks(self):
        self.assertEqual(hw.solve_distinct_disks(4, 2), [(0, 2), (2, 3), (1, 2)])
        self.assertEqual(hw.solve_distinct_disks(5, 2), [(0, 2), (1, 3), (2, 4)])
        self.assertEqual(hw.solve_distinct_disks(4, 3), [(1, 3), (0, 1), (2, 0),\
            (3, 2), (1, 3), (0, 1)])
        self.assertEqual(hw.solve_distinct_disks(5, 3), [(2, 3), (0, 2), (2, 4), (3, 2), (1, 3)])

    # DOMINOES ALPHA-BETA SECTION 4 #
    def test_create_dominoes_game(self):
        g = hw.create_dominoes_game(2, 2)
        self.assertEqual(g.get_board(), [[False, False], [False, False]])
        g = hw.create_dominoes_game(2, 3)
        self.assertEqual(g.get_board(), [[False, False, False], [False, False, False]])

    def test_reset(self):
        g = hw.DominoesGame([[False, False], [False, False]])
        g.reset()
        self.assertEqual(g.get_board(), [[False, False], [False, False]])
        g = hw.DominoesGame([[True, False], [True, False]])
        g.reset()
        self.assertEqual(g.get_board(), [[False, False], [False, False]])

    def test_is_legal_move(self):
        b = [[False, False], [False, False]]
        g = hw.DominoesGame(b)
        self.assertTrue(g.is_legal_move(0, 0, True))
        self.assertTrue(g.is_legal_move(0, 0, False))
        b = [[True, False], [True, False]]
        g = hw.DominoesGame(b)
        self.assertFalse(g.is_legal_move(0,0,False))
        self.assertTrue(g.is_legal_move(0,1,True))
        self.assertFalse(g.is_legal_move(1,1,True))

    def test_legal_moves(self):
        g = hw.create_dominoes_game(3, 3)
        self.assertEqual(list(g.legal_moves(True)), [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)])
        self.assertEqual(list(g.legal_moves(False)), [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)])
        b = [[True, False], [True, False]]
        g = hw.DominoesGame(b)
        self.assertEqual(list(g.legal_moves(True)), [(0, 1)])
        self.assertEqual(list(g.legal_moves(False)), [])

    def test_perform_moves(self):
        g = hw.create_dominoes_game(3, 3)
        g.perform_move(0, 1, True)
        self.assertEqual(g.get_board(), [[False, True,  False], [False, True,  False], [False, False, False]])
        g = hw.create_dominoes_game(3, 3)
        g.perform_move(1, 0, False)
        self.assertEqual(g.get_board(), [[False, False,  False], [True, True,  False], [False, False, False]])
        g.perform_move(0, 1, True)
        self.assertEqual(g.get_board(), [[False, False,  False], [True, True,  False], [False, False, False]])

    def test_game_over(self):
        g = hw.create_dominoes_game(2, 2)
        self.assertFalse(g.game_over(True))
        self.assertFalse(g.game_over(False))
        b = [[True, False], [True, False]]
        g = hw.DominoesGame(b)
        self.assertTrue(g.game_over(False))
        self.assertFalse(g.game_over(True))

    def test_dominoes_copy(self):
        g = hw.create_dominoes_game(4, 4)
        g2 = g.copy()
        self.assertEqual(g.get_board(), g2.get_board())
        g.perform_move(0, 0, True)
        self.assertNotEqual(g.get_board(), g2.get_board())

    def test_dominoes_successors(self):
        g = hw.create_dominoes_game(2, 2)
        move_results = [(0,0), (0,1)]
        board_results = [[[True, False], [True, False]], [[False, True], [False, True]]]
        i = 0
        for move, new_g in g.successors(True):
            self.assertEqual(move, move_results[i])
            self.assertEqual(new_g.get_board(), board_results[i])
            i += 1
        b = [[True, False], [True, False]]
        g = hw.DominoesGame(b)
        move_results = [(0,1)]
        board_results = [[[True, True], [True, True]]]
        i = 0
        for move, new_g in g.successors(True):
            self.assertEqual(move, move_results[i])
            self.assertEqual(new_g.get_board(), board_results[i])
            i += 1
        
    
    def test_best_move(self):
        pass

if __name__ == '__main__':
    unittest.main()