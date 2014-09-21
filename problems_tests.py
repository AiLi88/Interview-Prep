import unittest
from problems import *

class ProblemTest(unittest.TestCase):
    def test_merge_a_and_b_length(self):
        a = [1, 2, 3, 4, 5]
        b = [2, 3, 4]
        mergeArray(a, b)
        self.assertEqual(8, len(a))
    def test_simple_case_of_short_length(self):
        a = []
        b = [1]
        mergeArray(a, b)
        self.assertEqual(b, a)
    def test_existing_arrays_of_just_appending_b(self):
        a = [1]
        b = [2, 3, 4, 5]
        mergeArray(a, b)
        self.assertEqual([1, 2, 3, 4, 5], a)
    def test_appending_b_in_front_of_a(self):
        a = [2]
        b = [1]
        mergeArray(a, b)
        self.assertEqual([1,2], a)

if __name__ == '__main__':
    unittest.main()
