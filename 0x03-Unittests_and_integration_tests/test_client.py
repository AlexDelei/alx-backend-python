#!/usr/bin/env python3
"""
Unittests for Client
"""
import unittest
from unittest.mock import PropertyMock, patch, MagicMock, Mock
from parameterized import parameterized
GithubOrgClient = __import__('client').GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Parameterize and patch as decorators
    """

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json', return_value={'payload': True})
    def test_org(self, org_name, mock_get_json):
        """Tests that GithubOrgClient returns the correct values
        """
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, {'payload': True})
        mock_get_json.assert_called_once_with(f'https://api.github.com/orgs/{org_name}')

    @patch.object(GithubOrgClient, 'org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """Mocking a Property
        """
        # defining the mocked payload
        mock_payload = {'repos_url': "https://api.github.com/orgs/testorg/repos"}

        # setting the return value of the mocked org property
        mock_org.return_value = mock_payload

        # Instatiating the client
        client = GithubOrgClient('testorg')

        # _public_repos_url returns the expected url
        self.assertEqual(client._public_repos_url, "https://api.github.com/orgs/testorg/repos")


if __name__ == "__main__":
    unittest.main()
