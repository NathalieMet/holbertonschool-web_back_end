#!/usr/bin/env python3
"""
Class to test GithubOrgClient methods
"""

import unittest
from parameterized import parameterized
from client import GithubOrgClient
from unittest.mock import patch, Mock


class TestGithubOrgClient(unittest.TestCase):
    """
    Class to test GithubOrgClient methods
    """

    @patch('client.get_json')
    @parameterized.expand([
        ("google", "https://api.github.com/orgs/google"),
        ("abc", "https://api.github.com/orgs/abc"),
    ])
    def test_org(self, org_name, expected_url, mock_get_json):
        """
        This method tests that GithubOrgClient.org returns the correct
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

    def test_public_repos_url(self):
        """Test the _public_repos_url property"""

        # Payload to be returned by the mocked `org` method
        mock_payload = {"repos_url":
                        "https://api.github.com/orgs/google/repos"}

        # Use patch as a context manager to mock `GithubOrgClient.org`
        with patch.object(GithubOrgClient, 'org',
                          new_callable=property) as mock_org:
            # Set the return value of the mocked property
            mock_org.return_value = mock_payload

            # Create an instance of GithubOrgClient
            client = GithubOrgClient("google")

            # Call the _public_repos_url property
            result = client._public_repos_url

            # Assert that the _public_repos_url returns the expected URL
            self.assertEqual(result,
                             "https://api.github.com/orgs/google/repos")


if __name__ == "__main__":
    unittest.main()
