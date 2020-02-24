# import
import unittest
import HW3.jps6444 as hw

# create test class
class TestHWQuestions(unittest.TestCase):
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


if __name__ == '__main__':
    unittest.main()