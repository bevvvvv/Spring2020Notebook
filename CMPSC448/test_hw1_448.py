# import statements
import unittest
import pandas as pd
import HW1.hw1 as hw



class TestHWQuestions(unittest.TestCase):
    def setUp(self):
        self.data = [{'education': '11th', 'age': 33, 'sex': 'Male', 'native_country': 'United-States', 'income': '<=50K'},
                {'education': 'HS-grad', 'age': 40, 'sex': 'Male', 'native_country': 'United-States', 'income': '<=50K'},
                {'age': 60, 'sex': 'Male', 'native_country': 'England'},
                {'age': 55, 'sex': 'Female', 'native_country': 'England'},
                {'sex': 'Female', 'native_country': 'Russia'},
                {'sex': 'Female', 'native_country': 'England'},
                {'age': 26, 'native_country': 'United-States', 'income': '>50K'},
                {'age': 33, 'native_country': 'United-States', 'income': '>50K'},
                {'age': 36, 'native_country': 'United-States', 'income': '>50K'}]
        self.df = pd.DataFrame(self.data, index = range(len(self.data)))

    # return number of records in df that have
    # missing values for education
    def test_q1(self):
        self.assertEqual(hw.q1(self.df), 7) # number in test data
        df = self.df[pd.isna(self.df.education) == False]
        self.assertEqual(hw.q1(df), 0) # make sure zero is zero

    # return number of records in df where
    # age is between 40 and 60
    def test_q2(self):
        self.assertEqual(hw.q2(self.df), 3) # inclusive (number in test data)
        df = self.df[(self.df.age < 40) | (self.df.age > 60)]
        self.assertEqual(hw.q2(df), 0) # make sure zero is zero

    # return average age of males in df
    def test_q3(self):
        average = (33 + 40 + 60) / 3
        self.assertEqual(hw.q3(self.df), average) # average of test data
        df = self.df[self.df.sex == 'Female']
        self.assertEqual(hw.q3(df), 0) # make sure no males is zero

    # return number of females in df who
    # come from England
    def test_q4(self):
        self.assertEqual(hw.q4(self.df), 2) # number in test data
        df = self.df[self.df.native_country != 'England']
        self.assertEqual(hw.q4(df), 0) # check for zero

    # return standard deviation of ages
    # income should be above 50k and live in United-States
    def test_q5(self):
        import statistics as stat
        std = stat.stdev([26, 33, 36])
        self.assertEqual(hw.q5(self.df), std)

    # return true if those in workclass a who earn >50K
    # is greater than those in workclass b who earn >50K
    def test_q6(self):
        data = [{'workclass': 'Private', 'income': '>50K'},
                {'workclass': 'Private', 'income': '>50K'},
                {'workclass': 'Local-gov', 'income': '>50K'},
                {'workclass': 'Local-gov', 'income': '<=50K'},
                {'workclass': 'Local-gov', 'income': '<=50K'},
                {'workclass': 'Local-gov', 'income': '<=50K'},
                {'workclass': 'Private', 'income': '<=50K'}]
        df = pd.DataFrame(data, index = range(len(data)))
        self.assertEqual(hw.q6(df, 'Private', 'Local-gov'), True)
        self.assertEqual(hw.q6(df, 'Local-gov', 'Private'), False)




if __name__ == '__main__':
    unittest.main()