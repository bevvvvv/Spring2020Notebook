# import statements
import unittest
import pandas as pd
import numpy as np
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
        self.assertTrue(np.isnan(hw.q3(df))) # make sure no males is nan

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
        df = self.df[(self.df.income == '<=50K')]
        self.assertTrue(np.isnan(hw.q5(df)))

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
        # test if a is equal
        df = df[1:][['workclass', 'income']]
        self.assertEqual(hw.q6(df, 'Private', 'Local-gov'), False)

    # return nuber of people who work >20 hours a week
    # and earn <50K in income
    def test_q7(self):
        data = [{'income': '<=50K', 'hours_per_week': 20},
                {'income': '<=50K', 'hours_per_week': 45},
                {'income': '>50K', 'hours_per_week': 20},
                {'income': '>50K', 'hours_per_week': 999},
                {'income': '<=50K', 'hours_per_week': 18},
                {'income': '<=50K', 'hours_per_week': 0}]
        df = pd.DataFrame(data, index = range(len(data)))
        self.assertEqual(hw.q7(df), 2)
        # test zero
        df = df[2:][['income', 'hours_per_week']]
        self.assertEqual(hw.q7(df), 0)

    # returns average work hours for income >50k
    # United-States, Canada, India, England, Germany
    def test_q8(self):
        data = [{'income': '>50K', 'native_country': 'United-States', 'hours_per_week': 0},
                {'income': '>50K', 'native_country': 'United-States', 'hours_per_week': 10},
                {'income': '>50K', 'native_country': 'United-States', 'hours_per_week': 15},
                {'income': '<=50K', 'native_country': 'United-States', 'hours_per_week': 9999},
                {'income': '>50K', 'native_country': 'Canada', 'hours_per_week': 0},
                {'income': '>50K', 'native_country': 'Canada', 'hours_per_week': 20},
                {'income': '<=50K', 'native_country': 'Canada', 'hours_per_week': 9999},
                {'income': '<=50K', 'native_country': 'India', 'hours_per_week': 2}]
        df = pd.DataFrame(data, index = range(len(data)))
        output = {'United-States': (25 / 3), 'Canada': 10.0, 'India': np.nan, 'England': 0.0, 'Germany': 0.0}
        self.assertEqual(hw.q8(df), output)


if __name__ == '__main__':
    unittest.main()