#!/usr/bin/env python3
"""
Unittests for Client
"""
import unittest
from unittest.mock import patch, MagicMock, Mock
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


if __name__ == "__main__":
    unittest.main()
