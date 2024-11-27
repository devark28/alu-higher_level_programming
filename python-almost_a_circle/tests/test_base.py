#!/usr/bin/python3
"""
Test Base class
"""
import unittest

from models.base import Base
from models.rectangle import Rectangle


class BaseTest(unittest.TestCase):
    """
    Test Base class
    """

    def test_auto_ids(self):
        """
        Test auto ids
        """
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_manual_ids(self):
        """
        Test manual ids
        """
        b1 = Base(98)
        self.assertEqual(b1.id, 98)

    def test_ids_is_None(self):
        """
        Test ids is None
        """
        b1 = Base(None)
        b2 = Base(None)
        b3 = Base(None)
        self.assertEqual(b1.id, b3.id - 2)

    def test_to_json_string(self):
        """
        Test to_json_string
        """

        r1 = Rectangle(10, 7, 8, 6)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(type(json_dictionary), str)
        self.assertEqual(len(json_dictionary), 53)

    def test_to_json_string_empty(self):
        """
        Test to_json_string empty
        """
        json_dictionary = Base.to_json_string([])
        self.assertEqual(json_dictionary, "[]")

    def test_to_json_string_None(self):
        """
        Test to_json_string None
        """
        json_dictionary = Base.to_json_string(None)
        self.assertEqual(json_dictionary, "[]")

    def test_to_json_string_single_dict(self):
        """
        Test to_json_string single dict
        """
        dict_input = [{'id': 12}]
        json_output = Base.to_json_string(dict_input)
        self.assertEqual(json_output, '[{"id": 12}]')


if __name__ == '__main__':
    unittest.main()
