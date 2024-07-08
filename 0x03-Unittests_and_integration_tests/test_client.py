#!/usr/bin/env python3
"""
Unittests for Client
"""
import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized
GithubOrgClient = __import__('client').GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Parameterize and patch as decorators
    """

    @parameterized.expand([
        ("google", {'key': 'val'}),
        ('abc', {'key', 'val'})
    ])
    @patch('client.get_json', return_value={})
    def test_org(self, org_name, expected, mock_get_json):
        """Tests that GithubOrgClient returns the correct values
        """
        client = GithubOrgClient(org_name)

        # configuring the return value
        mock_get_json.return_value = expected

        result = client.org

        # comparing the results
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
