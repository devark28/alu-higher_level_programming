#!/usr/bin/python3
"""
Test Base class
"""
import unittest

from models.base import Base


class BaseTest(unittest.TestCase):
    """
    Test Base class
    """

    def test_auto_ids(self):
        """
        Test auto ids
        """
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_manual_ids(self):
        """
        Test manual ids
        """
        b1 = Base(98)
        b2 = Base(99)
        b3 = Base(100)
        self.assertEqual(b1.id, 98)
        self.assertEqual(b2.id, 99)
        self.assertEqual(b3.id, 100)

    def test_ids_is_None(self):
        """
        Test ids is None
        """
        b1 = Base(None)
        b2 = Base(None)
        b3 = Base(None)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)


if __name__ == '__main__':
    unittest.main()
