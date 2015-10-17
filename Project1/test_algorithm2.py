from file_loader.file_loader import load_lists_from_file
from algorithm2.algorithm2 import better_enumeration
import unittest


class Algorithm2Test(unittest.TestCase):

    def test_algorithm2_providedInput_shouldReturnMatchProvidedOutput(self):
        test_lists = load_lists_from_file('Problems/MSS_TestProblems-1.txt')
        expected = [(3, 14, 34), (0, 5, 30), (6, 12, 50), (2, 7, 187), (0, 4, 7), (0, 3, 210), (3, 7, 6)]
        actual = []
        for test_list in test_lists:
            actual.append(better_enumeration(test_list))
        message = "For the instructor provided input, should return the max sum of the provided output \n%s, but was \n%s" % (expected, actual)

        self.assertEqual(expected, actual, message)
