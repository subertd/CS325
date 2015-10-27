import unittest
from problem8.problem8 import Problem8


class TestProblem8(unittest.TestCase):

    problem8 = Problem8()

    def test_get_V_of_length_for_modifier(self):
        length = 10
        modifier = 1

        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        actual = self.problem8.get_V_of_length_for_modifier(length, modifier)

        self.assertEqual(expected, actual)
