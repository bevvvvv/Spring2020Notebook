import io
import sys
import unittest
import hopehw4 as hw

class TestHW(unittest.TestCase):
    def test_one(self):
        stub_stdin(self, '42')
        stub_stdin(self, '')
        stub_stdouts(self)
        hw.__main__()
        self.assertEqual(sys.stdout.getvalue(), '42\n')



def stub_stdin(testcase_inst, inputs):
    stdin = sys.stdin

    def cleanup():
        sys.stdin = stdin

    testcase_inst.addCleanup(cleanup)
    sys.stdin = StringIO(inputs)

def stub_stdouts(testcase_inst):
    stderr = sys.stderr
    stdout = sys.stdout

    def cleanup():
        sys.stderr = stderr
        sys.stdout = stdout

    testcase_inst.addCleanup(cleanup)
    sys.stderr = StringIO()
    sys.stdout = StringIO()

class StringIO(io.StringIO):
    """
    A "safely" wrapped version
    """

    def __init__(self, value=''):
        value = value.encode('utf8', 'backslashreplace').decode('utf8')
        io.StringIO.__init__(self, value)

    def write(self, msg):
        io.StringIO.write(self, msg.encode(
            'utf8', 'backslashreplace').decode('utf8'))