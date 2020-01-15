# import statements
import unittest
import pandas as pd
import HW1.hw1 as hw



class TestHWQuestions(unittest.TestCase):
    def setUp(self):
        self.data = [{'education': '11th', 'age': 33},
                {'education': 'HS-grad', 'age': 40},
                {'age': 60},
                {'age': 55}]
        self.df = pd.DataFrame(self.data, index = range(len(self.data)))

    # return number of records in df that have
    # missing values for education
    def test_q1(self):
        self.assertEqual(hw.q1(self.df), 2)

    # return number of records in df where
    # age is between 40 and 60
    def test_q2(self):
        self.assertEqual(hw.q2(self.df), 3) # inclusive


if __name__ == '__main__':
    unittest.main()