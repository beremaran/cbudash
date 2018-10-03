#!/usr/bin/env python3

import time
import unittest

from cbudash.caching import RequestCache


class TestCache(unittest.TestCase):

    def setUp(self):
        super().setUp()

        self.cache = RequestCache()

    def tearDown(self):
        super().tearDown()

        self.cache = None

    def test_empty_cache_does_not_have_key(self):
        self.assertFalse(self.cache.has('non-existing-key'))

    def test_empty_cache_returns_none_for_non_existing_keys(self):
        self.assertIsNone(self.cache.get('non-existing-key'))

    def test_empty_cache_returns_default_value_for_non_existing_keys(self):
        self.assertEqual(self.cache.get('non-existing-key', default='default-value'), 'default-value')

    def test_cache_is_mutable(self):
        key = 'existing-key'
        value = {'hello': 'world!'}
        self.cache.set(key, value)

        self.assertIsNotNone(self.cache.get(key, default=None))
        self.assertEqual(self.cache.get(key), value)

    def test_cache_is_expiring(self):
        key = 'something-something'
        value = 'expire me'
        self.cache.set(key, value, lifetime=2)
        time.sleep(2)
        self.assertIsNone(self.cache.get(key, default=None))


if __name__ == "__main__":
    unittest.main()
