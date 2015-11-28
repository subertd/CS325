from graph_formatter.graph_formatter import parse_input, format_output
from distance_calculator.distance_calculator import get_distance
import unittest


class MyTestCase(unittest.TestCase):

    TEST_POINTS = [(0, 0), (1, 3), (6, 0)]

    def test_parseInputTakesADictionaryAndReturnsATupleOfTwoLists(self):
        actual = parse_input({})
        assert isinstance(actual, tuple)
        (list1, list2) = actual
        assert isinstance(list1, list)
        assert isinstance(list2, list)

    def test_parseInputReturnsCompleteGraphVE(self):
        num_test_points = len(self.TEST_POINTS)
        input_dictionary = {}
        for i in range(0, num_test_points):
            input_dictionary[i] = self.TEST_POINTS[i]

        (actual_v, actual_e) = parse_input(input_dictionary)

        exp_num_v = num_test_points
        exp_num_e = 2 * (exp_num_v * ( exp_num_v - 1)) / 2

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
                    expected = ((i, j), get_distance(self.TEST_POINTS[i], self.TEST_POINTS[j]))
                    self.assertTrue(expected in actual_e)

    def test_formatOutputTakesATupleOfTwoListsAndReturnsAString(self):
        actual = format_output(([], []))
        assert isinstance(actual, basestring)


if __name__ == '__main__':
    unittest.main()
