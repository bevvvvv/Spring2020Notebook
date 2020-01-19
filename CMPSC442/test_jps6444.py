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
        test_input = [[1, 2], [3, 4]]
        test_output = [1, 2, 3, 4]
        self.assertEqual(hw.concatenate(test_input), test_output)
        test_input = ["abc", (0, [0])]
        test_output = ['a', 'b', 'c', 0, [0]]
        self.assertEqual(hw.concatenate(test_input), test_output)

    def test_transpose(self):
        test_input = [[1, 2, 3]]
        test_output = [[1], [2], [3]]
        self.assertEqual(hw.transpose(test_input), test_output)
        test_input = [[1, 2], [3, 4], [5, 6]]
        test_output = [[1, 3, 5], [2, 4, 6]]
        self.assertEqual(hw.transpose(test_input), test_output)

    ############################################################
    # Section 3: Sequence Slicing
    ############################################################

    def test_copy(self):
        test_input = "abc"
        test_output = "abc"
        self.assertEqual(hw.copy(test_input), test_output)
        test_input = (1, 2, 3)
        test_output = (1, 2, 3)
        self.assertEqual(hw.copy(test_input), test_output)
        test_input = [0, 0, 0]
        test_output = [0, 0, 0]
        case = hw.copy(test_input)
        test_input[0] = 1
        self.assertNotEqual(test_input, test_output)

    def test_all_but_last(self):
        test_input = "abc"
        test_output = 'ab'
        self.assertEqual(hw.all_but_last(test_input), test_output)
        test_input = (1, 2, 3)
        test_output = (1, 2)
        self.assertEqual(hw.all_but_last(test_input), test_output)
        test_input = ""
        test_output = ""
        self.assertEqual(hw.all_but_last(test_input), test_output)
        test_input = []
        test_output = []
        self.assertEqual(hw.all_but_last(test_input), test_output)

    def test_every_other(self):
        test_input = [1, 2, 3, 4, 5]
        test_output = [1, 3, 5]
        self.assertEqual(hw.every_other(test_input), test_output)
        test_input = "abcde"
        test_output = 'ace'
        self.assertEqual(hw.every_other(test_input), test_output)
        test_input = "abcdef"
        test_output = 'ace'
        self.assertEqual(hw.every_other(test_input), test_output)
        test_input = [1, 2, 3, 4, 5, 6]
        test_output = [1, 3, 5]
        self.assertEqual(hw.every_other(test_input), test_output)

    ############################################################
    # Section 4: Combinatorial Algorithms
    ############################################################

    def test_prefixes(self):
        test_input = [1, 2, 3]
        test_output = [[], [1], [1, 2], [1, 2, 3]]
        self.assertEqual(list(hw.prefixes(test_input)), test_output)
        test_input = "abc"
        test_output = ['', 'a', 'ab', 'abc']
        self.assertEqual(list(hw.prefixes(test_input)), test_output)

    def test_suffixes(self):
        test_input = [1, 2, 3]
        test_output = [[1, 2, 3], [2, 3], [3], []]
        self.assertEqual(list(hw.suffixes(test_input)), test_output)
        test_input = "abc"
        test_output = ['abc', 'bc', 'c', '']
        self.assertEqual(list(hw.suffixes(test_input)), test_output)

    def test_slices(self):
        test_input = [1, 2, 3]
        test_output = [[1], [1, 2], [1, 2, 3], [2], [2, 3], [3]]
        self.assertEqual(list(hw.slices(test_input)), test_output)
        test_input = "abc"
        test_output = ['a', 'ab', 'abc', 'b', 'bc', 'c']
        self.assertEqual(list(hw.slices(test_input)), test_output)

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