import unittest
from io.graph_parser import GraphParser


class GraphParserTest(unittest.TestCase):

    v1 = [(0, 0), (1, 3), (6, 0)]
    v2 = [(1, 3), (6, 0), (0, 0)]
    expected = [3, 6, 6]

    def test_TheSameTwoPointsHaveDistance0Between(self):
        actual = GraphParser().get_distance(self.v1[0], self.v1[0])
        self.assertEqual(0, actual)

    def test_APointAndAnother200PlusYHasDistance200(self):
        v1 = self.v1[0]
        (v2x, v2y) = v1
        test_point = (v2x, v2y + 200)

        expected = 200
        actual = GraphParser().get_distance(v1, test_point)

        self.assertEqual(expected, actual)

    def test_APointAndAnother200MinusYHasDistance200(self):
        v1 = self.v1[0]
        (v2x, v2y) = v1
        test_point = (v2x, v2y - 200)

        expected = 200
        actual = GraphParser().get_distance(v1, test_point)

        self.assertEqual(expected, actual)

    def test_APointAndAnother200PlusXHasDistance200(self):
        v1 = self.v1[0]
        (v2x, v2y) = v1
        test_point = (v2x + 200, v2y)

        expected = 200
        actual = GraphParser().get_distance(v1, test_point)

        self.assertEqual(expected, actual)

    def test_APointAndAnother200MinusXHasDistance200(self):
        v1 = self.v1[0]
        (v2x, v2y) = v1
        test_point = (v2x - 200, v2y)

        expected = 200
        actual = GraphParser().get_distance(v1, test_point)

        self.assertEqual(expected, actual)

    def test_theDistanceBetween2PointsIsTheRoundedRouteOfTheSumOfSquaresOfTheDifferenceBetweenXAndY(self):

        for i in range(len(self.expected)):
            actual = GraphParser().get_distance(self.v1[i], self.v2[i])
            self.assertEqual(self.expected[i], actual)


if __name__ == '__main__':
    unittest.main()
