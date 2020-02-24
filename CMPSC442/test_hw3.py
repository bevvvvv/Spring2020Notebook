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


if __name__ == '__main__':
    unittest.main()