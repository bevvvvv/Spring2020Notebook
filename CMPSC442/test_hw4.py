"""
HW 4 Testing
CMPSC442 Spam Filter (Naive Bayes Classifier)
"""
import unittest
import HW4.jps6444 as hw

class TestHWQuestions(unittest.TestCase):
    def setUp(self):
        self.ham_dir = 'train/ham/'
        self.spam_dir = 'train/spam/'

    def test_load_tokens(self):
        # given tests
        self.assertEqual(hw.load_tokens(self.ham_dir+'ham1')[200:204], ['of', 'my', 'outstanding', 'mail'])
        self.assertEqual(hw.load_tokens(self.ham_dir+'ham2')[110:114],['for', 'Preferences', '-', "didn't"])
        self.assertEqual(hw.load_tokens(self.spam_dir+'spam1')[1:5],['You', 'are', 'receiving', 'this'])
        self.assertEqual(hw.load_tokens(self.spam_dir+'spam2')[:4],['<html>', '<body>', '<center>', '<h3>'])

if __name__ == '__main__':
    unittest.main()