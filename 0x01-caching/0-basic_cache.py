#!/usr/bin/env python3
"""
basic caching system with no size limit
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    basic caching system with no size limit
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is None or item is None:
            pass

        self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key
        """
        if key is None:
            return None
        return self.cache_data.get(key)
