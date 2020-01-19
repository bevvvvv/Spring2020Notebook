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
        test_input = "This is an example."
        test_output = 'this is an example.'
        self.assertEqual(hw.normalize(test_input), test_output)
        test_input = "   EXTRA   SPACE   "
        test_output = 'extra space'
        self.assertEqual(hw.normalize(test_input), test_output)

    def test_no_vowels(self):
        test_input = "This is an example."
        test_output = 'Ths s n xmpl.'
        self.assertEqual(hw.no_vowels(test_input), test_output)
        test_input = "We love Python!"
        test_output = 'W lv Pythn!'
        self.assertEqual(hw.no_vowels(test_input), test_output)

    def test_digits_to_words(self):
        test_input = "Zip Code: 19104"
        test_output = 'one nine one zero four'
        self.assertEqual(hw.digits_to_words(test_input), test_output)
        test_input = "Pi is 3.1415..."
        test_output = 'three one four one five'
        self.assertEqual(hw.digits_to_words(test_input), test_output)
        test_input = "123456789"
        test_output = 'one two three four five six seven eight nine'
        self.assertEqual(hw.digits_to_words(test_input), test_output)
        test_input = "Pi is..."
        test_output = ''
        self.assertEqual(hw.digits_to_words(test_input), test_output)

    def test_to_mixed_case(self):
        test_input = "to_mixed_case"
        test_output = 'toMixedCase'
        self.assertEqual(hw.to_mixed_case(test_input), test_output)
        test_input = "__EXAMPLE__NAME__"
        test_output = 'exampleName'
        self.assertEqual(hw.to_mixed_case(test_input), test_output)

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