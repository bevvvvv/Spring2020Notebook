import io
import sys
import unittest

class TestHW(unittest.TestCase):
    def test_one(self):
        input_values = ['4 tbsp cocoa', '']
        output = []
    
        def mock_input(s):
            output.append(s)
            return input_values.pop(0)
        hw.input = mock_input
        hw.print = lambda s : output.append(s)

        hw.__main__()
        self.assertEqual(output, 'oof')



