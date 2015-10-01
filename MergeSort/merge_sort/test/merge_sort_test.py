import unittest
from merge_sort.merge_sort import get_middle, merge, merge_sort

__author__ = 'Don'


class MergeSortTest(unittest.TestCase):

    middle_message = "The middle index of a length %d list should be %d but was actually %f"
    merge_message = "The merged list of %s and %s should be %s but was actually %s"
    merge_sort_message = "The sorted list of %s should be %s but was actually %s"

    def testGetMiddle_5_shouldBe2(self):
        self.doTestMiddle(5, 2)

    def testGetMiddle_4_shouldBe2(self):
        self.doTestMiddle(4, 2)

    def testGetMiddle_3_shouldBe1(self):
        self.doTestMiddle(3, 1)

    def testGetMiddle_1_shouldBe0(self):
        self.doTestMiddle(1, 0)

    def testGetMiddle_0_shouldBe0(self):
        self.doTestMiddle(0, 0)

    def doTestMiddle(self, argument, expected):
        actual = get_middle(argument)
        message = MergeSortTest.middle_message % (argument, expected, actual)
        self.assertEqual(expected, actual, message)

    def testMerge_a1a5b2b7_shouldBe1_2_5_7(self):

        a = [1, 5]
        b = [2, 7]
        expected = [1, 2, 5, 7]

        self.doTestMerge(a, b, expected)

    def testMerge_a2a7b1b5_shouldBe1_2_5_7(self):

        a = [2, 7]
        b = [1, 5]
        expected = [1, 2, 5, 7]

        self.doTestMerge(a, b, expected)

    def doTestMerge(self, a, b, expected):
        actual = merge(a, b)
        message = MergeSortTest.merge_message % (a, b, expected, actual)
        self.assertEqual(expected, actual, message)

    def testMergeSort_5_3_1_7_2_shouldBe_1_2_3_5_7(self):
        argument = [5, 3, 1, 7, 2]
        expected = [1, 2, 3, 5, 7]
        self.doTestMergeSort(argument, expected)

    def doTestMergeSort(self, argument, expected):
        actual = merge_sort(argument)
        message = MergeSortTest.merge_sort_message % (argument, expected, actual)
        self.assertEqual(expected, actual, message)


def main():
    unittest.main()

if __name__ == '__main__':
    main()
