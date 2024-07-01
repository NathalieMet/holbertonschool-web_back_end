#!/usr/bin/env python3
"""In this task you will write the first unit test for utils.access_nested_map.

Create a TestAccessNestedMap class that inherits from unittest.TestCase.

Implement the TestAccessNestedMap.test_access_nested_map method to test that
the method returns what it is supposed to.

Decorate the method with @parameterized.expand to test the function for
following inputs:

nested_map={"a": 1}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a", "b")
For each of these inputs, test with assertEqual that the function returns the
expected result.
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map
from utils import get_json
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """Test the access_nested_map function from utils"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test that access_nested_map returns the expected result"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b'),
    ])

    def test_access_nested_map_exception(self, nested_map, path, key):
        """Test that a KeyError is raised for the following inputs"""
        with self.assertRaises(KeyError) as cm:
             access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), f"'{key}'")

class TestGetJson(unittest.TestCase):
    """Test the utils.get_json function from utils"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        # Configure the mock response
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        # Call the function under test
        result = get_json(test_url)

        # Assertions
        self.assertEqual(result, test_payload)
        mock_get.assert_called_once_with(test_url)

if __name__ == "__main__":
    unittest.main()
