#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_base_cases(self):
        """Tests for base cases"""
        self.assertEqual(max_integer([4, 90, 8, 22]), 90)
        self.assertEqual(max_integer([-1, -22, -3, -60]), -1)
        self.assertEqual(max_integer([11, 12, 13, 14, 15]), 15)
        self.assertEqual(max_integer([22, 0, -3, 8]), 22)
        self.assertEqual(max_integer([90, 0, 5, 7]), 90)
        self.assertEqual(max_integer([80]), 80)
        self.assertEqual(max_integer([]), None)

    def test_types(self):
        """Tests for type cases"""
        self.assertRaises(TypeError, max_integer, None)
        self.assertRaises(TypeError, max_integer, 7856) 
