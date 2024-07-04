#!/usr/bin/env python3
"""
Class to test GithubOrgClient methods
"""

import unittest
from parameterized import parameterized
from client import GithubOrgClient
from unittest.mock import patch, PropertyMock, Mock, MagicMock
from parameterized import parameterized_class


class TestGithubOrgClient(unittest.TestCase):
    """
    Class to test GithubOrgClient methods
    """

    @parameterized.expand([
        "google",
        "abc"
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str, mock_get_json: MagicMock):
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
        mock_get_json.assert_called_once_with(client.ORG_URL.format
                                              (org=client._org_name))

        # Assert that the return value is the mocked return value
        self.assertEqual(org_data, {"some_key": "some_value"})

    def test_public_repos_url(self):
        """Test the _public_repos_url property
        """

        # Payload to be returned by the mocked `org` method
        mock_payload = {"repos_url":
                        "https://api.github.com/orgs/google/repos"}

        # Use patch as a context manager to mock `GithubOrgClient.org`
        with patch.object(GithubOrgClient, 'org',
                          new_callable=PropertyMock) as mock_org:
            # Set the return value of the mocked property
            mock_org.return_value = mock_payload

            # Create an instance of GithubOrgClient
            client = GithubOrgClient("google")

            # Call the _public_repos_url property
            result = client._public_repos_url

            # Assert that the _public_repos_url returns the expected URL
            self.assertEqual(result,
                             "https://api.github.com/orgs/google/repos")

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test GithubOrgClient.public_repos
        """

        # Payload fictif pour les repos
        mock_repo_payload = [
            {"name": "repo1", "license": {"key": "mit"}},
            {"name": "repo2", "license": {"key": "apache-2.0"}},
        ]

        # Mock get_json pour retourner le payload de repos
        mock_get_json.return_value = mock_repo_payload

        # Mock _public_repos_url pour retourner une URL fictive
        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = (
                "https://api.github.com/orgs/google/repos"
            )

            # Créer une instance de GithubOrgClient
            client = GithubOrgClient("google")

            # Appeler public_repos et obtenir la liste de repos
            repos = client.public_repos()

            # Assertion sur le résultat de public_repos
            expected_repos = ["repo1", "repo2"]
            self.assertEqual(repos, expected_repos)

            # Vérifier que _public_repos_url a été appelé une fois
            mock_public_repos_url.assert_called_once()

            # Vérifier que get_json a été appelé une fois avec l'URL attendue
            mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/google/repos"
            )

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test that has_license returns the expected result"""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


org_payload = {
    "login": "google",
    "id": 1342004,
    "node_id": "MDEyOk9yZ2FuaXphdGlvbjEzNDIwMDQ=",
    "url": "https://api.github.com/orgs/google",
    "repos_url": "https://api.github.com/orgs/google/repos",
    # Add other necessary fields
}

repos_payload = [
    {
        "id": 1,
        "name": "repo1",
        "full_name": "google/repo1",
        "license": {"key": "apache-2.0"}
    },
    {
        "id": 2,
        "name": "repo2",
        "full_name": "google/repo2",
        "license": {"key": "mit"}
    }
    # Add other necessary fields
]

expected_repos = ["repo1", "repo2"]
apache2_repos = ["repo1"]


@parameterized_class([
    {
        "org_payload": org_payload,
        "repos_payload": repos_payload,
        "expected_repos": expected_repos,
        "apache2_repos": apache2_repos
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient methods
    """

    @classmethod
    def setUpClass(cls):
        """Set up class method to patch requests.get"""
        cls.get_patcher = patch('requests.get')
        mock_get = cls.get_patcher.start()

        # Configure the mock to return the appropriate fixture
        mock_get.side_effect = cls.get_side_effect

    @classmethod
    def tearDownClass(cls):
        """Tear down class method to stop patcher"""
        cls.get_patcher.stop()

    @staticmethod
    def get_side_effect(url):
        """Side effect method to return the appropriate fixture based on the
        URL"""
        if url == "https://api.github.com/orgs/google":
            return Mock(json=lambda: org_payload)
        if url == "https://api.github.com/orgs/google/repos":
            return Mock(json=lambda: repos_payload)
        return Mock(json=lambda: {})

    def test_public_repos(self):
        """Test the public_repos method"""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)
        self.assertEqual(client.public_repos("apache-2.0"), self.apache2_repos)


if __name__ == "__main__":
    unittest.main()
