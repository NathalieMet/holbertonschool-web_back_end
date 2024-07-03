#!/usr/bin/env python3
"""Class to test utils methods
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map
from utils import get_json
from utils import memoize
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
        """function test_get_json"""
        # Configure the mock response
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        # Call the function under test
        result = get_json(test_url)

        # Assertions
        self.assertEqual(result, test_payload)
        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Test the memoize function from utils
    """

    def test_memoize(self):
        """Function test for memoize
        """

        class TestClass:
            """Test class
            """

            def a_method(self):
                """Function a_method
                """
                return 42

            @memoize
            def a_property(self):
                """Function a_property
                """
                return self.a_method()

        # Créer une instance de TestClass
        test_instance = TestClass()

        # Patch a_method pour vérifier combien de fois il est appelé
        with patch.object(TestClass, 'a_method',
                          return_value=42) as mock_a_method:
            # Appeler a_property deux fois
            result1 = test_instance.a_property
            result2 = test_instance.a_property

            # Vérifier que les résultats sont corrects
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            # Vérifier que a_method n'a été appelé qu'une seule fois
            mock_a_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
