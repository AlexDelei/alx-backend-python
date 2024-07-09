#!/usr/bin/env python3
"""
Unittests for Client
"""
import unittest
from unittest.mock import PropertyMock, patch, MagicMock, Mock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Parameterize and patch as decorators
    """

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json', return_value={'payload': True})
    def test_org(self, org_: str, mock_get: Mock) -> None:
        """Tests that GithubOrgClient returns the correct values
        """
        client = GithubOrgClient(org_)
        self.assertEqual(client.org, {'payload': True})
        mock_get.assert_called_once_with(f'https://api.github.com/orgs/{org_}')

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """Mocking a Property
        """
        # defining the mocked payload
        mock_pyld = {'repos_url': "https://api.github.com/orgs/testorg/repos"}

        # setting the return value of the mocked org property
        mock_org.return_value = mock_pyld

        # Instatiating the client
        client = GithubOrgClient('testorg')

        # _public_repos_url returns the expected url
        self.assertEqual(
            client._public_repos_url,
            "https://api.github.com/orgs/testorg/repos"
            )
