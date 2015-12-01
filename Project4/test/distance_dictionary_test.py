from graph_formatter.distance_dictionary import DistanceDictionary
import random
import sys
import unittest


class MyTestCase(unittest.TestCase):

    LARGE_NUMBER = 15000 * (15000 - 1) / 2

    def test_something(self):
        subject = DistanceDictionary()

        subject[(1, 2)] = 5
        expected = 5
        actual = subject[(1, 2)]
        self.assertEqual(expected, actual)

    def test_orderOfIntsInTupleDoesNotMatter(self):
        subject = DistanceDictionary()

        subject[(1, 2)] = 5
        expected = 5
        actual = subject[(2, 1)]
        self.assertEqual(expected, actual)

        subject[(2, 1)] = 42
        expected = 42
        actual = subject[(1, 2)]
        self.assertEqual(expected, actual)

    def test_canHandleAVeryLargeNumberOfElements(self):
        subject = DistanceDictionary()

        for i in xrange(self.LARGE_NUMBER):
            for j in xrange(self.LARGE_NUMBER):
                subject[i, j] = random.randrange(-sys.maxint, sys.maxint)


if __name__ == '__main__':
    unittest.main()
