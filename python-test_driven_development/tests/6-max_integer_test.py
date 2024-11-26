#!/usr/bin/python3
"""
unittest for max_integer(list=[])
"""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Test cases for max_integer
    """

    def test_max_integer(self):
        """
        Test max_integer
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([1, 4, 3, 2]), 4)
        self.assertEqual(max_integer([1]),
                         1)
        self.assertEqual(max_integer([]), None)

        with self.assertRaises(TypeError):
            max_integer(1)
        with self.assertRaises(TypeError):
            max_integer([1, "hello"])
        with self.assertRaises(TypeError):
            max_integer([1, 2, 3, "hello"])

    def test_empty_list(self):
        """
        Test empty list
        """
        self.assertEqual(max_integer([]), None)

    def test_string(self):
        """
        Test string
        """
        self.assertEqual(max_integer("hello"), 'o')
        self.assertEqual(max_integer("hello world"), 'w')

    def test_float(self):
        """
        Test float
        """
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4]), 4.4)
        self.assertEqual(max_integer([4.4, 3.3, 2.2, 1.1]), 4.4)
        self.assertEqual(max_integer([1.1, 4.4, 3.3, 2.2]), 4.4)
        self.assertEqual(max_integer([1.1]), 1.1)
        self.assertEqual(max_integer([]), None)

        with self.assertRaises(TypeError):
            max_integer(1.1)
        with self.assertRaises(TypeError):
            max_integer([1.1, "hello"])
