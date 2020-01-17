# import
import unittest
import HW1.jps6444 as hw

# create test class
class TestHWQuestions(unittest.TestCase):
    ############################################################
    # Section 2: Working with Lists
    ############################################################

    # l: list
    # p: boolean predicate
    # f: function to apply
    def test_extract_and_apply(self):
        test_list = [0, 1, 2, 3, 4, 5]
        test_predicate = lambda x: x >= 3
        test_function = lambda x: x - 3
        self.assertEqual(hw.extract_and_apply(test_list, test_predicate, test_function), [0,1,2])

    def test_concatenate(self):
        pass

    def test_transpose(self):
        pass

    ############################################################
    # Section 3: Sequence Slicing
    ############################################################

    def test_copy(self):
        pass

    def test_all_but_last(self):
        pass

    def test_every_other(self):
        pass

    ############################################################
    # Section 4: Combinatorial Algorithms
    ############################################################

    def test_prefixes(self):
        pass

    def test_suffixes(self):
        pass

    def test_slices(self):
        pass

    ############################################################
    # Section 5: Text Processing
    ############################################################

    def test_normalize(self):
        pass

    def test_no_vowels(self):
        pass

    def test_digits_to_words(self):
        pass

    def test_to_mixed_case(self):
        pass

    ############################################################
    # Section 6: Polynomials
    ############################################################

    def test__init__(self):
        pass

    def test_get_polynomial(self):
        pass

    def test__neg__(self):
        pass

    def test__add__(self):
        pass

    def test__sub__(self):
        pass

    def test__mul__(self):
        pass

    def test__call__(self):
        pass

    def test_simplify(self):
        pass

    def test__str__(self):
        pass

# main function
if __name__ == '__main__':
    unittest.main()