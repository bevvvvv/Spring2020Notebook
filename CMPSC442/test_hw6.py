"""
HW 6 Testing
CMPSC442 HMM POS Taggin
"""
import unittest
import HW6.jps6444 as hw

class TestHWQuestions(unittest.TestCase):
    def setUp(self):
        self.corpus = './CMPSC442/HW6/brown-corpus.txt'
        return super().setUp()

    def test_load_corpus(self):
        c = hw.load_corpus(self.corpus)
        self.assertEqual(c[1402], [('It', 'PRON'), ('made', 'VERB'), ('him', 'PRON'), ('human', 'NOUN'), ('.', '.')])
        self.assertEqual(c[1799], [('The', 'DET'), ('prospects', 'NOUN'), ('look', 'VERB'), ('great', 'ADJ'), ('.', '.')])

    def test_most_probable_tags(self):
        c = hw.load_corpus(self.corpus)
        t = hw.Tagger(c)
        self.assertEqual(t.most_probable_tags(["The", "man", "walks", "."]), ['DET', 'NOUN', 'VERB', '.'])
        self.assertEqual(t.most_probable_tags(["The", "blue", "bird", "sings"]), ['DET', 'ADJ', 'NOUN', 'VERB'])


if __name__ == '__main__':
    unittest.main()