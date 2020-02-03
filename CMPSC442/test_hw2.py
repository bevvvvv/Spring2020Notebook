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

    ############################################################
    # Section 2: Lights Out
    ############################################################
    def test__init__(self):
        pass

    def test_get_board(self):
        pass

    def test_perform_move(self):
        pass

    def test_scramble(self):
        pass

    def test_is_solved(self):
        pass

    def test_copy(self):
        pass

    def test_successors(self):
        pass

    def test_find_solution(self):
        pass

    def test_create_puzzle(self):
        pass

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