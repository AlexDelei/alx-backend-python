#!/usr/bin/env python3
"""
Parameterizing a unit test
"""
import unittest
from parameterized import parameterized
from typing import Mapping, Sequence
access_nested_map = __import__('utils').access_nested_map


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


if __name__ == '__main__':
    unittest.main()
