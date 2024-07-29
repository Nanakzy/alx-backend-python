#!/usr/bin/env python3
"""
Module for GithubOrgClient unit and integration tests.
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Test suite for GithubOrgClient.
    """

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json', return_value={"payload": True})
    def test_org(self, org_name, mock_get_json):
        """
        Test that GithubOrgClient.org returns the correct value.
        """
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, {"payload": True})
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    @patch.object(GithubOrgClient, 'org', new_callable=property)
    def test_public_repos_url(self, mock_org):
        """
        Test_public_repos_url returns the correct URL based on org payload.
        """
        mock_org.return_value = {"repos_url": "http://example.com/repos"}
        client = GithubOrgClient('org_name')
        self.assertEqual(client._public_repos_url, "http://example.com/repos")

    @patch('client.get_json', return_value=[
        {"name": "repo1"}, {"name": "repo2"}
    ])
    @patch.object(GithubOrgClient, '_public_repos_url', new_callable=property)
    def test_public_repos(self, mock_repos_url, mock_get_json):
        """
        Test that public_repos returns the correct list of repositories.
        """
        mock_repos_url.return_value = "http://example.com/repos"
        client = GithubOrgClient('org_name')
        self.assertEqual(client.public_repos(), ["repo1", "repo2"])
        mock_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with("http://example.com/repos")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """
        Test that has_license returns the correct boolean based on license key.
        """
        client = GithubOrgClient('org_name')
        self.assertEqual(client.has_license(repo, license_key), expected)


fixtures = {
    "org_payload": {"repos_url": "http://example.com/repos"},
    "repos_payload": [{"name": "repo1"}, {"name": "repo2"}],
    "expected_repos": ["repo1", "repo2"],
    "apache2_repos": [{"name": "repo1", "license": {"key": "apache-2.0"}}]
}


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"), [
        (fixtures["org_payload"], fixtures["repos_payload"],
         fixtures["expected_repos"], fixtures["apache2_repos"])
    ]
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration test suite for GithubOrgClient.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the class by patching requests.get.
        """
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()
        cls.mock_get.return_value.json.side_effect = [
            cls.org_payload, cls.repos_payload
        ]

    @classmethod
    def tearDownClass(cls):
        """
        Tear down the class by stopping the patcher.
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """
        Test that public_repos returns the correct list of repositories
        based on the fixtures.
        """
        client = GithubOrgClient('org_name')
        self.assertEqual(client.public_repos(), self.expected_repos)


if __name__ == '__main__':
    unittest.main()
