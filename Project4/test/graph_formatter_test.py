from graph_formatter.graph_formatter import parse_input, format_output
from distance_calculator.distance_calculator import get_distance
import sys
import random
import unittest


class MyTestCase(unittest.TestCase):

    TEST_POINTS = [(0, 0), (1, 3), (6, 0)]

    def test_parseInputTakesADictionaryAndReturnsATupleOfAListAndADictionary(self):
        actual = parse_input({})
        assert isinstance(actual, tuple)
        (expected_list, expected_dict) = actual
        assert isinstance(expected_list, list)
        assert isinstance(expected_dict, dict)

    def test_parseInputReturnsCompleteGraphVE(self):
        num_test_points = len(self.TEST_POINTS)
        input_dictionary = {}
        for i in range(0, num_test_points):
            input_dictionary[i] = self.TEST_POINTS[i]

        (actual_v, actual_e) = parse_input(input_dictionary)

        exp_num_v = num_test_points
        exp_num_e = 2 * (exp_num_v * (exp_num_v - 1)) / 2

        act_num_v = len(actual_v)
        act_num_e = len(actual_e)

        self.assertEqual(exp_num_v, act_num_v)
        self.assertEqual(exp_num_e, act_num_e)

    def test_parseInputReturnsTheCorrectSetOfVertices(self):
        num_test_points = len(self.TEST_POINTS)
        input_dictionary = {}
        for i in range(0, num_test_points):
            input_dictionary[i] = self.TEST_POINTS[i]

        (actual_v, actual_e) = parse_input(input_dictionary)
        for i in range(0, num_test_points):
            self.assertTrue(i in actual_v)

    def test_parseInputReturnsEdgesWhichContainTheSourceTargetAndDistance(self):
        num_test_points = len(self.TEST_POINTS)
        input_dictionary = {}
        for i in range(0, num_test_points):
            input_dictionary[i] = self.TEST_POINTS[i]

        (actual_v, actual_e) = parse_input(input_dictionary)

        for i in range(0, num_test_points):
            for j in range(0, num_test_points):
                if i != j:
                    expected_key = (i, j)
                    expected_value = get_distance(self.TEST_POINTS[i], self.TEST_POINTS[j])
                    self.assertEqual(expected_value, actual_e[expected_key])

    def test_formatOutputTakesADictionaryOfTotalIntAndOrderListIntAndReturnsAString(self):
        test_solution = {
            'total': 0,
            'order': [0]
        }
        actual = format_output(test_solution)
        assert isinstance(actual, basestring)

    def test_formatOutputPutsTheTotalDistanceOnTheTopLine(self):
        for i in [-1000000, -1, 0, 1, 1000000]:
            test_solution = {
                'total': i,
                'order': [3, 0, 1, 2]
            }
            expected = '%d\n' % i
            actual = format_output(test_solution)
            assert actual.startswith(expected)

    def test_formatOutputPutsTheTheNextVertexInOrderOnSubsequentLines(self):
        for i in range(100):
            expected = '0\n'
            test_solution = {
                'total': 0,
                'order': []
            }
            for j in range(i):
                rand = random.randrange(-sys.maxint, sys.maxint)
                test_solution['order'].append(rand)
                expected = "%s%d\n" % (expected, rand)

            actual = format_output(test_solution)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
