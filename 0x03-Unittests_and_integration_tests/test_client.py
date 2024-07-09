#!/usr/bin/env python3
"""
Unittests for Client
"""
import unittest
import fixtures
from unittest.mock import PropertyMock, patch, MagicMock, Mock
from parameterized import parameterized, parameterized_class
from typing import Dict
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

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, tst_dict: Dict, lcns: str, expec: bool) -> None:
        """Parameterize to test for a bool return value"""
        self.assertEqual(
            GithubOrgClient('google').has_license(tst_dict, lcns),
            expec
            )


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    fixtures.TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test
    """
    @classmethod
    def setUpClass(cls) -> None:
        """This method sets up test environment before any tests run
        """
        cls.get_patcher = patch("requests.get")
        cls.mock_get = cls.get_patcher.start()

        def side_effect(url):
            """
            Defines how the mock should behave depending on URL
            requested
            """
            class MockResponse:
                """
                A nested class simulating the response object
                returned by requests.get().json().
                It has a json method that returns json_data.
                """
                def __init__(self, data) -> None:
                    """Initiate with passed data"""
                    self.json_data = data

                def json(self):
                    """Returns the JSON data"""
                    return self.json_data

            if url.endswith('orgs/google'):
                return MockResponse(cls.org_payload)
            elif url.endswith("orgs/google/repos"):
                return MockResponse(cls.repos_payload)
            else:
                return None

        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls) -> None:
        """Cleans up after all tests have run and restores
        `requests.get` to its original state
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test public repos
        """
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Testing public repos with license
        """
        client = GithubOrgClient("google")
        self.assertEqual(
            client.public_repos(license="apache-2.0"),
            self.apache2_repos
            )
