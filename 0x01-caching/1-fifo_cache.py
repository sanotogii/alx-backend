#!/usr/bin/env python3
"""
FIFO caching system
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFO cashing system
    """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        add an item in the cache
        """
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) > self.MAX_ITEMS:
                oldest_key = next(iter(self.cache_data))
                del self.cache_data[oldest_key]
                print(f"DISCARD: {oldest_key}")
            self.cache_data[key] = item

    def get(self, key):
        """
        get an item by key
        """
        return self.cache_data.get(key)
