from file_loader.file_loader import load_lists_from_file
from algorithm3.algorithm3 import divide_and_conquer, max_crossing_subarray
import unittest


class Algorithm3Test(unittest.TestCase):

    def test_algorithm1_providedInput_shouldReturnMatchProvidedOutput(self):
        test_lists = load_lists_from_file('Problems/MSS_TestProblems-1.txt')
        expected = [(3, 14, 34), (0, 5, 30), (6, 12, 50), (2, 7, 187), (0, 4, 7), (0, 3, 210), (3, 7, 6)]
        actual = []
        for test_list in test_lists:
            actual.append(divide_and_conquer(test_list))
        message = "For the instructor provided input, should return the max sum of the provided output \n%s, but was \n%s" % (expected, actual)

        self.assertEqual(expected, actual, message)

    def test_max_crossing_subarray(self):

        test_list = [2, -1, -3, 5]
        p = 0
        q = 2
        r = 4

        expected_max_left = 0
        expected_max_right = 3
        expected_sum = 3

        expected = [expected_max_left, expected_max_right, expected_sum]
        actual = max_crossing_subarray(test_list, p, q, r)
        message = "for %s p = %d q = %d r = %d, expected %s, but received %s" % (test_list, p, q, r, expected, actual)

        self.assertEqual(expected, actual, message)
