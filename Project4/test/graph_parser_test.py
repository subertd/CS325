import unittest
from io.graph_parser import GraphParser


class GraphParserTest(unittest.TestCase):

    TEST_POINT_1 = (200, 600)

    def test_TheSameTwoPointsHaveDistance0Between(self):
        v1 = self.TEST_POINT_1
        v2 = self.TEST_POINT_1

        expected = 0
        actual = GraphParser().get_distance(v1, v2)

        self.assertEqual(expected, actual)

    def test_APointAndAnother200PlusYHasDistance200(self):
        v1 = self.TEST_POINT_1
        (v2x, v2y) = self.TEST_POINT_1
        v2 = (v2x, v2y + 200)

        expected = 200
        actual = GraphParser().get_distance(v1, v2)

        self.assertEqual(expected, actual)

    def test_APointAndAnother200MinusYHasDistance200(self):
        v1 = self.TEST_POINT_1
        (v2x, v2y) = self.TEST_POINT_1
        v2 = (v2x, v2y - 200)

        expected = 200
        actual = GraphParser().get_distance(v1, v2)

        self.assertEqual(expected, actual)

    def test_APointAndAnother200PlusXHasDistance200(self):
        v1 = self.TEST_POINT_1
        (v2x, v2y) = self.TEST_POINT_1
        v2 = (v2x + 200, v2y)

        expected = 200
        actual = GraphParser().get_distance(v1, v2)

        self.assertEqual(expected, actual)

    def test_APointAndAnother200MinusXHasDistance200(self):
        v1 = self.TEST_POINT_1
        (v2x, v2y) = self.TEST_POINT_1
        v2 = (v2x - 200, v2y)

        expected = 200
        actual = GraphParser().get_distance(v1, v2)

        self.assertEqual(expected, actual)

    def test_theDistanceBetween2PointsIsTheRoundedRouteOfTheSumOfSquaresOfTheDifferenceBetweenXAndY(self):
        v1 = [(0, 0), (1, 3), (6, 0)]
        v2 = [(1, 3), (6, 0), (0, 0)]
        expected = [3, 6, 6]

        for i in range(len(expected)):
            actual = GraphParser().get_distance(v1[i], v2[i])
            self.assertEqual(expected[i], actual)


if __name__ == '__main__':
    unittest.main()
