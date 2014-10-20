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
    def test_swap_elements_without_temp(self):
        x = 20
        y = 30
        x, y = swap_num(x, y)
        self.assertEqual(20, y)
        self.assertEqual(30, x)
    def test_won_game_of_tic_tac_toe(self):
        board = [
            ['x', 'x', 'x'],
            [-1, 'o', 'x'],
            [-1, -1, 'o']
        ]
        self.assertEqual('x', won_game(board))
        board = [
            ['o', 'x', 'x'],
            ['o', 'o', 'x'],
            ['o', -1, 'o']
        ]
        self.assertEqual('o', won_game(board))
        board = [
            ['o', 'x', 'x'],
            ['x', 'o', 'x'],
            ['o', -1, 'o']
        ]
        self.assertEqual('o', won_game(board))
        board = [
            ['o', 'o', 'x'],
            ['o', 'x', 'x'],
            ['x', -1, 'o']
        ]
        self.assertEqual('x', won_game(board))
        board = [
            [-1, -1, -1],
            [-1, -1, -1],
            [-1, -1, -1]
        ]
        self.assertEqual(-1, won_game(board))
    def test_trailing_zeros_in_factorial(self):
        self.assertEqual(1, trailing_zeros(5))
        self.assertEqual(2, trailing_zeros(10))
        self.assertEqual(2, trailing_zeros(12))
        self.assertEqual(3, trailing_zeros(15))
    def test_max_num_without_conditional_or_comparison(self):
        self.assertEqual(5, max_num(5, 4))
        self.assertEqual(100, max_num(99, 100))
        self.assertEqual(10000, max_num(10, 10000))
        self.assertEqual(200, max_num(124, 200))
    def test_indicies_of_array_to_sort(self):
        self.assertEqual((-1,-1), find_indicies([]))
        a = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
        self.assertEqual((3,9), find_indicies(a))
    def test_contigious_sum_of_array(self):
        self.assertEqual(0, find_contiguous_sequence([]))
        self.assertEqual(5, find_contiguous_sequence([2,-8,3,-2,4,-10]))
        self.assertEqual(5, find_contiguous_sequence([1,2,-4,1,3,-2,3,-1]))

if __name__ == '__main__':
    unittest.main()
