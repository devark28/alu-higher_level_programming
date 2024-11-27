#!/usr/bin/python3
"""
Test Rectangle class
"""
import unittest

from models.rectangle import Rectangle


class RectangleTest(unittest.TestCase):
    """
    Test Rectangle class
    """

    def test_rect_with_2(self):
        """
        Test width
        """
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_rect_with_3(self):
        """
        Test width
        """
        r = Rectangle(1, 2, 3)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 0)

    def test_rect_with_4(self):
        """
        Test width
        """
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_rect_type_errors(self):
        """
        Test width
        """
        with self.assertRaises(TypeError):
            r = Rectangle("1", 2)

        with self.assertRaises(TypeError):
            r = Rectangle(1, "2")

        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, "3")

        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 3, "4")

    def test_rect_with_5_args(self):
        """
        Test width
        """
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 3, 4, 5)


if __name__ == '__main__':
    unittest.main()
