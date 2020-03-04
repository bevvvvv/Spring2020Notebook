import io
import sys
import unittest
import testSkeleton as hw

class TestHW(unittest.TestCase):
    def test_one(self):
        input_values = ['4 tbsp cocoa', '1/4 pound butter', '2 tsp corn syrup', '1 can evaporated milk'\
                        '1 tsp water', '', '16', '25']
        output = []
    
        def mock_input(s=None):
            if s != None:
                output.append(s)
            return input_values.pop(0)
        hw.input = mock_input
        hw.print = lambda *args : output.append(''.join([str(arg) for arg in args]))

        hw.main()

        self.assertEqual(output, ['This is a recipe scaler for serving large crowds!', 
                                  'Enter one ingredient per line, with a numeric value first.', 
                                  'Indicate the end of input with an empty line.', 
                                  '    4       tbsp cocoa', 
                                  '  1/4      pound butter', 
                                  '    2        tsp corn syrup', 
                                  '    1        can evaporated milk1 tsp water', 
                                  'How many does this recipe serve? ', 
                                  'How many people must be served? ', 
                                  'Multiplying the recipe by 2', 
                                  '    8       tbsp cocoa', 
                                  '  2/4      pound butter', 
                                  '    4        tsp corn syrup', 
                                  '    2        can evaporated milk1 tsp water'])



