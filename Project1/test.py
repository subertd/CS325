from algorithm1.algorithm1 import enumeration
from algorithm2.algorithm2 import better_enumeration
from algorithm3.algorithm3 import divide_and_conquer
from algorithm4.algorithm4 import dynamic_programming
from file_loader.file_loader import load_lists_from_file
from file_writer.file_writer import FileWriter

import unittest

class IntegratedTest(unittest.TestCase):

    def test_algorithm1_providedInput_shouldReturnMatchProvidedOutput(self):
        test_lists = load_lists_from_file('Problems/MSS_TestProblems-1.txt')
        expected = [34, 30, 50, 187, 7, 210, 6]
        actual = []
        for test_list in test_lists:
            actual.append(enumeration(test_list))
        message = "For the instructor provided input, should return the max sum of the provided output %s, but was %s" % (expected, actual)

        self.assertEqual(expected, actual, message)

"""
#print test
for list in test:
    print enumeration(list)
    print better_enumeration(list)
    print divide_and_conquer(list)
    """