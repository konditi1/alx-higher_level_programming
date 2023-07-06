#!/usr/bin/python3
"""
Test suite for the max_integer function
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Test suite for the max_integer function.
    """

    def test_empty_list(self):
        """
        Test for an empty list.
        """
        self.assertEqual(max_integer([]), None)

    def test_single_element_list(self):
        """
        Test for a list with a single element.
        """
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([-5]), -5)

    def test_positive_numbers(self):
        """
        Test for a list of positive numbers.
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([10, 2, 8, 5]), 10)
        self.assertEqual(max_integer([100, 200, 300, 150]), 300)

    def test_negative_numbers(self):
        """
        Test for a list of negative numbers.
        """
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-10, -2, -8, -5]), -2)
        self.assertEqual(max_integer([-100, -200, -300, -150]), -100)

    def test_mixed_numbers(self):
        """
        Test for a list of mixed positive and negative numbers.
        """
        self.assertEqual(max_integer([-10, 2, -8, 5]), 5)
        self.assertEqual(max_integer([-100, 200, -300, 150]), 200)
        self.assertEqual(max_integer([-10, -2, 8, 5]), 8)

    def test_duplicate_numbers(self):
        """
        Test for a list with duplicate numbers.
        """
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)
        self.assertEqual(max_integer([-5, -5, -5, -5]), -5)
        self.assertEqual(max_integer([10, 10, 10, 10]), 10)


if __name__ == '__main__':
    unittest.main()
