#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test class for the max_integer function"""

    def test_regular_list(self):
        """Test with a regular list of positive integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_start(self):
        """Test with max at the start of the list"""
        self.assertEqual(max_integer([10, 2, 3, 4]), 10)

    def test_max_at_middle(self):
        """Test with max in the middle of the list"""
        self.assertEqual(max_integer([1, 3, 10, 2]), 10)

    def test_max_at_end(self):
        """Test with max at the end of the list"""
        self.assertEqual(max_integer([1, 2, 3, 10]), 10)

    def test_empty_list(self):
        """Test with an empty list - should return None"""
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        """Test with a single-element list"""
        self.assertEqual(max_integer([5]), 5)

    def test_all_negative(self):
        """Test with all negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_positive_negative(self):
        """Test with mixed positive and negative numbers"""
        self.assertEqual(max_integer([-1, 0, 1, 2]), 2)

    def test_all_same(self):
        """Test with all elements the same"""
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_floats(self):
        """Test with floats"""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_mixed_int_float(self):
        """Test with mixed integers and floats"""
        self.assertEqual(max_integer([1, 2.5, 3]), 3)

    def test_two_elements(self):
        """Test with two-element list"""
        self.assertEqual(max_integer([1, 2]), 2)

    def test_default_empty(self):
        """Test with no argument (uses default empty list)"""
        self.assertIsNone(max_integer())


if __name__ == '__main__':
    unittest.main()
