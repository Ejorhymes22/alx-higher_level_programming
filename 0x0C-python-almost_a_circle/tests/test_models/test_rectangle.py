#!/usr/bin/python3
"""
contains tests for rectangle class
"""


import unittest
import inspect
import pep8
import json
from models import rectangle
from models.base import Base
Rectangle = rectangle.Rectangle



class TestRectangleDocs(unittest.TestCase):
    """Tests the rectangle style and doc"""
    def test_pep8_conformance_base(self):
        """Test that models/base.py conforms to pep*"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0,
                        "Found code style errors (and warnings).")

    def test_docs(self):
        """Tests documentations"""
        self.assertTrue(len(Rectangle.__doc__) >= 1)
        self.assertTrue(len(rectangle.__doc__) >= 1)

class TestRectangle(unittest.TestCase):
    """Test for functionality of rectangle class"""
    def test_normal_value(self):
        """test for normal value"""
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(1, 2, 3, 4, 12)
        self.assertEqual(r2.id, 12)

        r3 = Rectangle(3, 5)
        self.assertEqual(r3.id, 2)

    def test_rea(self):
        r1 = Rectangle(1, 4)
        self.assertEqual(r1.area(), 4)

        r2 = Rectangle(2, 5)
        self.assertEqual(r2.area(), 10)

    def test_update(self):
        """tests for updates"""
        r1 = Rectangle(10, 10)
        r1.update(89)
        self.assertEqual(r1.id, 89)

        r1.update(height=20)
        self.assertEqual(r1.height, 20)

    def test_or_args(self):
        """tests for many args"""
        with self.assertRaises(TypeError):
            rec = Rectangle(1, 2, 3, 4, 5, 5, 1)

        with self.assertRaises(ValueError):
            rec = Rectangle(-1, 3)

        with self.assertRaises(ValueError):
            rec = Rectangle(1, -4)

        with self.assertRaises(TypeError):
            rec = Rectangle('a', 9)
