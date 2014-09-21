import unittest
from algorithms import *

class SortingTest(unittest.TestCase):
    def setUp(self):
        self.random_ = [[x for x in generate_(10, 100)] for y in range(100)]
    def test_Bubble_Sort(self):
        self.assertTrue(run_algorithm(self.random_, bubblesort))
    def test_Selection_Sort(self):
        self.assertTrue(run_algorithm(self.random_, selection_sort))
    def test_Insertion_Sort(self):
        self.assertTrue(run_algorithm(self.random_, insertion_sort))
    def test_Shell_Sort(self):
        self.assertTrue(run_algorithm(self.random_, shell_sort))
    def test_Merge_Sort(self):
        random = self.random_[0]
        merge_sort(random)

if __name__ == '__main__':
    unittest.main()

