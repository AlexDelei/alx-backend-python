#!/usr/bin/env python3
"""
Parameterizing a unit test
"""
import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from typing import Mapping, Sequence
access_nested_map = __import__('utils').access_nested_map
get_json = __import__('utils').get_json


class TestAccessNestedMap(unittest.TestCase):
    """
    Parameterize a unit test
    """

    @parameterized.expand([
        ({'a': 1}, ['a'], 1),
        ({"a": {"b": 2}}, ['a'], {"b": 2}),
        ({"a": {"b": 2}}, ['a', 'b'], 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping, keys: Sequence, exp):
        """Parameterize a Unit test"""
        self.assertEqual(access_nested_map(nested_map, keys), exp)

    @parameterized.expand([
        ({}, ['a'], KeyError),
        ({'a': 1}, ['a', 'b'], KeyError)
    ])
    def test_access_nested_map_exception(self, n: Mapping, kys: Sequence, exp):
        """Parameterize a unit test"""
        with self.assertRaises(exp):
            access_nested_map(n, kys)


class TestGetJson(unittest.TestCase):
    """
    Mock HTTP calls
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(self, url, results, mock_get):
        """Mock http calls"""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'payload': results['payload']}

        mock_get.return_value = mock_response
        response = get_json(url)
        self.assertEqual(response, {'payload': results['payload']})


if __name__ == '__main__':
    unittest.main()
