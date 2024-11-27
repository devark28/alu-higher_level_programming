#!/usr/bin/python3
"""
Test Rectangle class
"""
import sys
import unittest
from io import StringIO

from models.rectangle import Rectangle


class RectangleTest(unittest.TestCase):

    def test_rect_with_2(self):
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_rect_with_3(self):
        r = Rectangle(1, 2, 3)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 0)

    def test_rect_with_4(self):
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_rect_with_5(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 3)
        # self.assertEqual(r.id, 3)


# @unittest.skip
class RectangleTestErrors(unittest.TestCase):

    def test_rect_type_errors_1(self):
        with self.assertRaises(TypeError):
            r = Rectangle("1", 2)

    def test_rect_type_errors_2(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1, "2")

    def test_rect_type_errors_3(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, "3")

    def test_rect_type_errors_4(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 3, "4")

    def test_rect_value_errors_1(self):
        with self.assertRaises(ValueError):
            r = Rectangle(-1, 2)

    def test_rect_value_errors_2(self):
        with self.assertRaises(ValueError):
            r = Rectangle(1, -2)

    def test_rect_value_errors_3(self):
        with self.assertRaises(ValueError):
            r = Rectangle(0, 2)

    def test_rect_value_errors_4(self):
        with self.assertRaises(ValueError):
            r = Rectangle(1, 0)

    def test_rect_value_errors_5(self):
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, -3)

    def test_rect_value_errors_6(self):
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, 3, -4)

    def test_rectangle_area(self):
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)

    def test_rectangle_str_representation(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_rectangle_display(self):
        r1 = Rectangle(2, 3)
        captured_output = StringIO()
        sys.stdout = captured_output
        r1.display()
        sys.stdout = sys.__stdout__

        expected_output = "##\n##\n##\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_rectangle_display_with_x(self):
        r2 = Rectangle(3, 2, 1)
        captured_output = StringIO()
        sys.stdout = captured_output
        r2.display()
        sys.stdout = sys.__stdout__

        expected_output = " ###\n ###\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_rectangle_display_with_x_and_y(self):
        r3 = Rectangle(2, 3, 2, 2)
        captured_output = StringIO()
        sys.stdout = captured_output
        r3.display()
        sys.stdout = sys.__stdout__

        expected_output = "\n\n  ##\n  ##\n  ##\n"
        self.assertEqual(captured_output.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()
