"""
HW 4 Testing
CMPSC442 Spam Filter (Naive Bayes Classifier)
"""
import unittest
import HW4.jps6444 as hw

class TestHWQuestions(unittest.TestCase):
    def setUp(self):
        self.ham_dir = './CMPSC442/HW4/train/ham'
        self.spam_dir = './CMPSC442/HW4/train/spam'

    def test_load_tokens(self):
        # given tests
        self.assertEqual(hw.load_tokens(self.ham_dir+'/ham1')[200:204], ['of', 'my', 'outstanding', 'mail'])
        self.assertEqual(hw.load_tokens(self.ham_dir+'/ham2')[110:114],['for', 'Preferences', '-', "didn't"])
        self.assertEqual(hw.load_tokens(self.spam_dir+'/spam1')[1:5],['You', 'are', 'receiving', 'this'])
        self.assertEqual(hw.load_tokens(self.spam_dir+'/spam2')[:4],['<html>', '<body>', '<center>', '<h3>'])

    def test_log_probs(self):
        paths = [self.ham_dir+"ham%d" % i for i in range(1, 11)]
        p = hw.log_probs(paths, 1e-5)
        self.assertEqual(p['the'], -3.6080194731874062)
        self.assertEqual(p['line'], -4.272995709320345)
        paths = [self.spam_dir+"spam%d" % i for i in range(1, 11)]
        p = hw.log_probs(paths, 1e-5)
        self.assertEqual(p['Credit'], -5.837004641921745)
        self.assertEqual(p['<UNK>'], -20.34566288044584)
    
    def test_is_spam(self):
        sf = hw.SpamFilter(self.spam_dir, self.ham_dir, 1e-5)
        self.assertTrue(sf.is_spam(self.spam_dir + '/spam1'))
        self.assertTrue(sf.is_spam(self.spam_dir + '/spam2'))
        sf = hw.SpamFilter(self.spam_dir, self.ham_dir, 1e-5)
        self.assertFalse(sf.is_spam(self.ham_dir + '/ham1'))
        self.assertFalse(sf.is_spam(self.ham_dir + '/ham2'))

    def test_most_indicative_spam(self):
        sf = hw.SpamFilter(self.spam_dir, self.ham_dir, 1e-5)
        self.assertEqual(sf.most_indicative_spam(5), ['<a', '<input', '<html>', '<meta', '</head>'])

    def test_most_indicative_spam(self):
        sf = hw.SpamFilter(self.spam_dir, self.ham_dir, 1e-5)
        self.assertEqual(sf.most_indicative_ham(5), ['Aug', 'ilug@linux.ie', 'install', 'spam.', 'Group:'])

if __name__ == '__main__':
    unittest.main()