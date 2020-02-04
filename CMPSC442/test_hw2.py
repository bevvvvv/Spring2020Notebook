# import
import unittest
import HW2.jps6444 as hw

# create test class
class TestHWQuestions(unittest.TestCase):
    ############################################################
    # Section 1: N-Queens
    ############################################################

    def test_num_placements_all(self):
        self.assertEqual(hw.num_placements_all(2), 4)
        self.assertEqual(hw.num_placements_all(4), 256)
        self.assertEqual(hw.num_placements_all(8), 16777216)
        self.assertEqual(hw.num_placements_all(10), 10000000000)

    def test_num_placements_one_per_row(self):
        self.assertEqual(hw.num_placements_one_per_row(2), 2)
        self.assertEqual(hw.num_placements_one_per_row(4), 24)
        self.assertEqual(hw.num_placements_one_per_row(8), 40320)
        self.assertEqual(hw.num_placements_one_per_row(10), 3628800)

    def test_n_queens_valid(self):
        self.assertEqual(hw.n_queens_valid([0, 0]), False)
        self.assertEqual(hw.n_queens_valid([0, 2]), True)
        self.assertEqual(hw.n_queens_valid([0, 1]), False)
        self.assertEqual(hw.n_queens_valid([0, 3, 1]), True)

    def test_n_queens_solutions(self):
        solutions = hw.n_queens_solutions(4)
        self.assertEqual(next(solutions), [1, 3, 0, 2])
        self.assertEqual(next(solutions), [2, 0, 3, 1])
        self.assertEqual(list(hw.n_queens_solutions(6)), [[1, 3, 5, 0, 2, 4], \
            [2, 5, 1, 4, 0, 3], [3, 0, 4, 1, 5, 2], [4, 2, 0, 5, 3, 1]])
        self.assertEqual(len(list(hw.n_queens_solutions(8))), 92)

    ############################################################
    # Section 2: Lights Out
    ############################################################
    def test_get_board_init(self):
        b = [[True, False], [False, True]]
        p = hw.LightsOutPuzzle(b)
        self.assertEqual(p.get_board(), [[True, False], [False, True]])
        b = [[True, True], [True, True]]
        p = hw.LightsOutPuzzle(b)
        self.assertEqual(p.get_board(), [[True, True], [True, True]])
        b = [[True, False, True], [True, True, False]]
        p = hw.LightsOutPuzzle(b)
        self.assertEqual(p.get_board(), [[True, False, True], [True, True, False]])
        self.assertEqual(p.m, 2)
        self.assertEqual(p.n, 3)

    def test_perform_move(self):
        p = hw.create_puzzle(3, 3)
        p.perform_move(1, 1)
        self.assertEqual(p.get_board(), [[False, True, False], [True,  True, True ], \
            [False, True, False]])
        p.perform_move(0, 0)
        self.assertEqual(p.get_board(), [[True, False, False], [False,  True, True ], \
            [False, True, False]])

    def test_scramble(self):
        import random
        random.seed(1738)
        p = hw.create_puzzle(3, 3)
        p.scramble()
        self.assertEqual(p.get_board(), [[False, False, False], [True, True, False], \
            [False, False, False]])
        
    def test_is_solved(self):
        b = [[True, False], [False, True]]
        p = hw.LightsOutPuzzle(b)
        self.assertFalse(p.is_solved())
        b = [[False, False], [False, False]]
        p = hw.LightsOutPuzzle(b)
        self.assertTrue(p.is_solved())


    def test_copy(self):
        p = hw.create_puzzle(3, 3)
        p2 = p.copy()
        self.assertEqual(p.get_board(), p2.get_board())
        p = hw.create_puzzle(3, 3)
        p2 = p.copy()
        p.perform_move(1, 1)
        self.assertNotEqual(p.get_board(), p2.get_board())

    def test_successors(self):
        pass

    def test_find_solution(self):
        pass

    def test_create_puzzle(self):
        p = hw.create_puzzle(2, 2)
        self.assertEqual(p.get_board(), [[False, False], [False, False]])
        p = hw.create_puzzle(2, 3)
        self.assertEqual(p.get_board(), [[False, False, False], [False, False, False]])

    ############################################################
    # Section 3: Linear Disk Movement
    ############################################################

    def test_solve_identical_disks(self):
        pass

    def test_solve_distinct_disks(self):
        pass

    # main function
if __name__ == '__main__':
    unittest.main()