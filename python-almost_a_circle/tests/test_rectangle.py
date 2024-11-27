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

    def test_rect_type_errors_1(self):
        """
        Test type errors
        """
        with self.assertRaises(TypeError):
            r = Rectangle("1", 2)

    def test_rect_type_errors_2(self):
        """
        Test type errors
        """
        with self.assertRaises(TypeError):
            r = Rectangle(1, "2")

    def test_rect_type_errors_3(self):
        """
        Test type errors
        """
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, "3")

    def test_rect_type_errors_4(self):
        """
        Test type errors
        """
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 3, "4")

    def test_rect_with_5_args(self):
        """
        Test width
        """
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 3, 4, 5)

    """
    Test of Rectangle(-1, 2) exists
    
    Test of Rectangle(1, -2) exists
    
    Test of Rectangle(0, 2) exists
    
    Test of Rectangle(1, 0) exists
    
    Test of Rectangle(1, 2, -3) exists
    
    Test of Rectangle(1, 2, 3, -4) exists
    """

    # def test_rect_value_errors(self):
    #     """
    #     Test value errors
    #     """
    #     with self.assertRaises(ValueError):
    #         r = Rectangle(-1, 2)
    #
    #     with self.assertRaises(ValueError):
    #         r = Rectangle(1, -2)
    #
    #     with self.assertRaises(ValueError):
    #         r = Rectangle(0, 2)
    #
    #     with self.assertRaises(ValueError):
    #         r = Rectangle


if __name__ == '__main__':
    unittest.main()
