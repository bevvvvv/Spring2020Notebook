"""
HW 5 Testing
CMPSC442 Markov Model
"""
import unittest
import HW5.jps6444 as hw

class TestHWQuestions(unittest.TestCase):
    def test_tokenize(self):
        """
        Highly reccommend adding edge cases.
        """
        self.assertEqual(hw.tokenize("  This is an example.  "), ['This', 'is', 'an', 'example', '.'])
        self.assertEqual(hw.tokenize("'Medium-rare,' she said."), ["'", 'Medium', '-', 'rare', ',', "'", 'she', 'said', '.'])


if __name__ == '__main__':
    unittest.main()