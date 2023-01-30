#!/usr/bin/env python3
"""Module: test_utils.py"""

import unittest
from unittest.mock import patch
from utils import access_nested_map, memoize
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """test the utils Module"""

    @parameterized.expand([
       ({"a": 1}, ("a",), 1),
       ({"a": {"b": 2}}, ("a",), {"b": 2}),
       ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """test access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """test access_nested_map function with exceptions"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """tests utils.get_json function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    def test_get_json(self, test_url, test_payload):
        """test get json method"""
        with patch('utils.get_json') as mock_get_json:
            mock_get_json.return_value = test_payload
            result = mock_get_json(test_url)
            mock_get_json.assert_called_once_with(test_url)

            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """test the utils.memoize function"""
    def test_memoize(self):
        """test memoize function"""

        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_a_method:
            test_class = TestClass()
            test_class.a_property()
            test_class.a_property()
            mock_a_method.assert_called_once()
