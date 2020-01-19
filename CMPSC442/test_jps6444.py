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
        test_input = [(2, 1), (1, 0)]
        p = hw.Polynomial(test_input)

    def test_get_polynomial(self):
        test_input = [(2, 1), (1, 0)]
        p = hw.Polynomial(test_input)
        self.assertEqual(p.get_polynomial(), ((2, 1), (1, 0)))

    def test__neg__(self):
        test_input = [(2, 1), (-1, 0)]
        p = hw.Polynomial(test_input)
        p = -p
        self.assertEqual(p.get_polynomial(), ((-2, 1), (1, 0)))
        p = -(-p)
        self.assertEqual(p.get_polynomial(), ((-2, 1), (1, 0)))

    def test__add__(self):
        test_input = [(2, 1), (1, 0)]
        p = hw.Polynomial(test_input)
        q = p + p
        self.assertEqual(q.get_polynomial(), ((2, 1), (1, 0), (2, 1), (1, 0)))
        q = hw.Polynomial([(4, 3), (3, 2)])
        r = p + q
        self.assertEqual(r.get_polynomial(), ((2, 1), (1, 0), (4, 3), (3, 2)))

    def test__sub__(self):
        test_input = [(2, 1), (1, 0)]
        p = hw.Polynomial(test_input)
        q = p - p
        self.assertEqual(q.get_polynomial(), ((2, 1), (1, 0), (-2, 1), (-1, 0)))
        q = hw.Polynomial([(4, 3), (3, 2)])
        r = p - q
        self.assertEqual(r.get_polynomial(), ((2, 1), (1, 0), (-4, 3), (-3, 2)))

    def test__mul__(self):
        p = hw.Polynomial([(2, 1), (1, 0)])
        q = hw.Polynomial([(4, 3), (3, 2)])
        r = p * p
        self.assertEqual(r.get_polynomial(), ((4, 2), (2, 1), (2, 1), (1, 0)))
        r = p * q
        self.assertEqual(r.get_polynomial(), ((8, 4), (6, 3), (4, 3), (3, 2)))

    def test__call__(self):
        p = hw.Polynomial([(2, 1), (1, 0)])
        self.assertEqual([p(x) for x in range(5)], [1, 3, 5, 7, 9])
        q = -(p * p) + p
        self.assertEqual([q(x) for x in range(5)], [0, -6, -20, -42, -72])

    def test_simplify(self):
        p = hw.Polynomial([(2, 1), (1, 0)])
        q = -p + (p * p)
        self.assertEqual(q.get_polynomial(), ((-2, 1), (-1, 0), (4, 2), (2, 1), (2, 1), (1, 0)))
        q.simplify()
        self.assertEqual(q.get_polynomial(), ((4, 2), (2, 1)))
        q = p - p
        self.assertEqual(q.get_polynomial(), ((2, 1), (1, 0), (-2, 1), (-1, 0)))
        q.simplify()
        self.assertEqual(q.get_polynomial(), ((0, 0),))

    def test__str__(self):
        p = hw.Polynomial([(1, 1), (1, 0)])
        qs = (p, p + p, -p, -p - p, p * p)
        for q in qs:
            q.simplify()
        self.assertEqual(str(qs[0]), 'x + 1')
        self.assertEqual(str(qs[1]), '2x + 2')
        self.assertEqual(str(qs[2]), '-x - 1')
        self.assertEqual(str(qs[3]), '-2x - 2')
        self.assertEqual(str(qs[4]), 'x^2 + 2x + 1')
        p = hw.Polynomial([(0, 1), (2, 3)])
        self.assertEqual(str(p), '0x + 2x^3')
        self.assertEqual(str(p * p), '0x^2 + 0x^4 + 0x^4 + 4x^6')
        self.assertEqual(str(-p * p), '0x^2 + 0x^4 + 0x^4 - 4x^6')
        q = hw.Polynomial([(1, 1), (2, 3)])
        self.assertEqual(str(q), 'x + 2x^3')
        self.assertEqual(str(q * q), 'x^2 + 2x^4 + 2x^4 + 4x^6')
        self.assertEqual(str(-q * q), '-x^2 - 2x^4 - 2x^4 - 4x^6')

# main function
if __name__ == '__main__':
    unittest.main()