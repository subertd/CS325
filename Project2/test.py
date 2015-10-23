from algorithm1.algorithm1 import changeslow
from algorithm2.algorithm2 import changegreedy
from algorithm3.algorithm3 import changedp
import unittest


class AlgorithmTest(unittest.TestCase):

    test_set_1 = ([1, 2, 4, 8], 15, [([1, 1, 1, 1], 4), ([1, 1, 1, 1], 4), ([1, 1, 1, 1], 4)])
    test_set_2 = ([1, 3, 7, 12], 29, [([0, 1, 2, 1], 4), ([2, 1, 0, 2], 5), ([0, 1, 2, 1], 4)])
    test_set_3 = ([1, 3, 7, 12], 31, [([0, 0, 1, 2], 3), ([0, 0, 1, 2], 3), ([0, 0, 1, 2], 3)])

    def test_changeslow_set1(self):
        V, A, expected_all = self.test_set_1
        expected = expected_all[0]
        actual = changeslow(V, A)
        self.assertEqual(expected, actual)
        
    def test_changeslow_set2(self):
        V, A, expected_all = self.test_set_2
        expected = expected_all[0]
        actual = changeslow(V, A)
        self.assertEqual(expected, actual)
        
    def test_changeslow_set3(self):
        V, A, expected_all = self.test_set_3
        expected = expected_all[0]
        actual = changeslow(V, A)
        self.assertEqual(expected, actual)

    def test_changegreedy_set1(self):
        V, A, expected_all = self.test_set_1
        expected = expected_all[1]
        actual = changegreedy(V, A)
        self.assertEqual(expected, actual)
        
    def test_changegreedy_set2(self):
        V, A, expected_all = self.test_set_2
        expected = expected_all[1]
        actual = changegreedy(V, A)
        self.assertEqual(expected, actual)
        
    def test_changegreedy_set3(self):
        V, A, expected_all = self.test_set_3
        expected = expected_all[1]
        actual = changegreedy(V, A)
        self.assertEqual(expected, actual)
        
    def test_changedp_set1(self):
        V, A, expected_all = self.test_set_1
        expected = expected_all[2]
        actual = changedp(V, A)
        self.assertEqual(expected, actual)
        
    def test_changedp_set2(self):
        V, A, expected_all = self.test_set_2
        expected = expected_all[2]
        actual = changedp(V, A)
        self.assertEqual(expected, actual)
        
    def test_changedp_set3(self):
        V, A, expected_all = self.test_set_3
        expected = expected_all[2]
        actual = changedp(V, A)
        self.assertEqual(expected, actual)