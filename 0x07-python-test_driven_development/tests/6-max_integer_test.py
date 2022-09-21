#!/usr/bin/python3
"""Unittest for max_integer([...])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """tests for max int"""
    def test_properlist(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, -4, 3, -3]), 3)
        self.assertEqual(max_integer(), None)

    def test_errors(self):
        self.assertRaises(TypeError, max_integer, [1, 'a', 2])
        self.assertRaises(TypeError, max_integer, 1234)
        self.assertRaises(TypeError, max_integer, [1, 2, 3, [1, 2]])
