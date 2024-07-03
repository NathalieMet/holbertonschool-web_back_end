#!/usr/bin/env python3
"""Class to test GithubOrgClient methods
"""

import unittest
from parameterized import parameterized
from client import GithubOrgClient
from unittest.mock import patch, Mock


class TestGithubOrgClient(unittest.TestCase):
    """Class to test GithubOrgClient methods"""

    @patch('client.get_json')
    @parameterized.expand([
        ("google", "https://api.github.com/orgs/google"),
        ("abc", "https://api.github.com/orgs/abc"),
    ])
    def test_org(self, org_name, expected_url, mock_get_json):
        """This method tests that GithubOrgClient.org returns the correct
        value"""

        # Mock the return value of get_json
        mock_get_json.return_value = {"some_key": "some_value"}

        # Create an instance of GithubOrgClient
        client = GithubOrgClient(org_name)

        # Call the org method
        org_data = client.org

        # Assert that get_json was called once with the expected URL
        mock_get_json.assert_called_once_with(expected_url)

        # Assert that the return value is the mocked return value
        self.assertEqual(org_data, {"some_key": "some_value"})


if __name__ == "__main__":
    unittest.main()
