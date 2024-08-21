#!/usr/bin/env python3
BaseCaching = __import__("base_caching").BaseCaching
"""
basic caching system with no size limit
"""


class BasicCache(BaseCaching):
    """
    basic caching system with no size limit
    """

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key
        """
        return self.cache_data.get(key)
