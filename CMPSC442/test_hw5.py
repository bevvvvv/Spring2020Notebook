"""
HW 5 Testing
CMPSC442 Markov Model
"""
import unittest
import random
import HW5.jps6444 as hw

class TestHWQuestions(unittest.TestCase):
    def test_tokenize(self):
        """
        Highly reccommend adding edge cases.
        """
        self.assertEqual(hw.tokenize("  This is an example.  "), ['This', 'is', 'an', 'example', '.'])
        self.assertEqual(hw.tokenize("'Medium-rare,' she said."), ["'", 'Medium', '-', 'rare', ',', "'", 'she', 'said', '.'])
        self.assertEqual(hw.tokenize('a b c d'), ['a', 'b', 'c', 'd'])

    def test_ngrams(self):
        self.assertEqual(hw.ngrams(1, ["a", "b", "c"]), [((), 'a'), ((), 'b'), ((), 'c'), ((), '<END>')])
        self.assertEqual(hw.ngrams(2, ["a", "b", "c"]), [(('<START>',), 'a'), (('a',), 'b'), (('b',), 'c'), (('c',), '<END>')])
        self.assertEqual(hw.ngrams(3, ["a", "b", "c"]), [(('<START>', '<START>'), 'a'), (('<START>', 'a'), 'b'), (('a', 'b'), 'c'), (('b', 'c'), '<END>')])

    def test_init_update_probs(self):
        m = hw.NgramModel(1)
        m.update('a b c d')
        m.update('a b a b')
        self.assertEqual(m.prob((), 'a'), 0.3)
        self.assertEqual(m.prob((), 'c'), 0.1)
        self.assertEqual(m.prob((), '<END>'), 0.2)

        m = hw.NgramModel(2)
        m.update('a b c d')
        m.update('a b a b')
        self.assertEqual(m.prob(("<START>",), "a"), 1.0)
        self.assertEqual(m.prob(("b",), "c"), (1/3))
        self.assertEqual(m.prob(("a",), "x"), 0.0)

    def test_random_token(self):
        m = hw.NgramModel(1)
        m.update('a b c d')
        m.update('a b a b')
        random.seed(1)
        result = [m.random_token(()) for i in range(25)]
        self.assertEqual(result, ['<END>', 'c', 'b', 'a', 'a', 'a', 'b', 'b', '<END>', '<END>', 'c', 'a', 'b', \
            '<END>', 'a', 'b', 'a', 'd', 'd', '<END>', '<END>', 'b', 'd', 'a', 'a'])

        m = hw.NgramModel(2)
        m.update('a b c d')
        m.update('a b a b')
        random.seed(2)
        result = [m.random_token(('<START>',)) for i in range(6)]
        self.assertEqual(result, ['a', 'a', 'a', 'a', 'a', 'a'])
        result = [m.random_token(('b',)) for i in range(6)]
        self.assertEqual(result, ['c', '<END>', 'a', 'a', 'a', '<END>'])


if __name__ == '__main__':
    unittest.main()