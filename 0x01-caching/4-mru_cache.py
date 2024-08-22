#!/usr/bin/env python3
"""
MRU caching system
"""
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """
    MRU caching system
    """

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is None or item is None:
            pass
        else:
            if key in self.cache_data:
                self.cache_data.move_to_end(key)
            elif len(self.cache_data) >= self.MAX_ITEMS:
                most_recent_key, _ = self.cache_data.popitem(last=True)
                print(f"DISCARD: {most_recent_key}")
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        else:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
