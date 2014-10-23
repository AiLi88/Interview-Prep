import unittest
import arrays_and_strings as a_s

class TestArraysAndString(unittest.TestCase):
    def test_unique_characters(self):
        self.assertFalse(a_s.unique_characters("123123"))
        self.assertFalse(a_s.unique_characters("aaa"))
        self.assertTrue(a_s.unique_characters(""))
        self.assertTrue(a_s.unique_characters("123"))
    def test_permutation_of_two_strings(self):
        self.assertTrue(a_s.permutation("abc", "cba"))
        self.assertTrue(a_s.permutation("abc", "bca"))
        self.assertTrue(a_s.permutation("abc", "abc"))
        self.assertTrue(a_s.permutation("", ""))
        self.assertFalse(a_s.permutation("a", "b"))
    def test_replace_space_with_encode(self):
        # string = "Mr John Smith   "
        # self.assertEqual("Mr%20John%20Smith", a_s.replace_space_with_encode(string))
        pass
    def test_string_compression_returns_string_smaller_than_original(self):
        # Pass in an empty string
        # Pass in a string that is smaller if compressed
        # Pass in a string that is bigger if compressed
        pass
    def test_rotate_matrix_by_90_degress(self):
        pass
    def test_set_entire_row_and_column_to_zero_if_element_is_zero(self):
        pass
    def test_check_if_string_is_rotation_of_another_string(self):
        self.assertTrue(a_s.is_rotation("waterbottle", "erbottlewat"))




if __name__ == '__main__':
    unittest.main()
