import unittest
from problems import *

class ProblemTest(unittest.TestCase):
    def test_FindNum(self):
#        a = [15,16,19,20,25,1,3,4,5,7,10,14]
#        self.assertEqual(10, pivotedBinarySearch(a, 10))
#        a = [1, 1, 1, 2, 4]
#        self.assertEqual(4, pivotedBinarySearch(a,  4))
        a = [2, 2, 2, 3, 4, 2]
        self.assertEqual(4, pivotedBinarySearch(a,  4))
    def test_find_String(self):
        self.assertEqual(-1, find_string(['','','','','','','',''], 'bar'))
        self.assertEqual(6, find_string(['a','','b','','','','bar'], 'bar'))
    def test_find_num_matrix(self):
        matrix = [
            [15, 20, 40, 85],
            [20, 35, 80, 95],
            [30, 55, 95, 105],
            [40, 80, 100, 120]
        ]
        self.assertEqual((2, 1), findNumMatrix(matrix, 55))
        self.assertEqual((0, 1), findNumMatrix(matrix, 20))
        self.assertEqual((-1, -1), findNumMatrix(matrix, 5))
    def test_find_longest_subsequence(self):
        find_subsequence([10,22,9,33,21,50,41,60,80])
    def test_find_repetition(self):
        a = [1, 1]
        self.assertEqual(True, find_repetition(a))
        a = [1, 2, 3, 1]
        self.assertEqual(True, find_repetition(a))
        a = []
        self.assertEqual(False, find_repetition(a))
    def test_find_kth_element(self):
        a = [20, 10, 5, 89, 4]
        self.assertEqual(20, kth_element(a, 0, len(a)-1, 4) )
if __name__ == '__main__':
    unittest.main()
