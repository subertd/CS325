import unittest
from algorithm3.algorithm3 import divide_and_conquer, max_crossing_subarray


class MmsTest(unittest.TestCase):

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
