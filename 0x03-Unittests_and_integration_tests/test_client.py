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

    @patch('client.get_json', return_value=[
            {'name': 'https://api.github.com/orgs/google/repos'},
            {'name': 'https://api.github.com/orgs/apple/repos'}
            ])
    def test_public_repos(self, mock_get_json) -> None:
        """More Patching
        """
        target = 'client.GithubOrgClient._public_repos_url'
        with patch(target, new_callable=PropertyMock) as mock_pblc:
            # Defining the mocked _public_repos_url return value
            mock_pblc.return_value = "https://api.github.com/orgs/test/repos"
            # Instatiate the client
            client = GithubOrgClient("test")
            # Call the method to test
            repo = client.public_repos()
            # Ensuring the list of repos is as expected
            for mr in mock_get_json:
                self.assertEqual(repo, mr['name'])
            # Ensure that Mocked property was called once
            mock_pblc.assert_called_once()
            mock_get_json.assert_called_once()


if __name__ == "__main__":
    unittest.main()
