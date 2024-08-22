#!/usr/bin/env python3
"""
LFU caching system
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """
    LFU caching system
    """

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()
        self.freq = OrderedDict()

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is None or item is None:
            pass
        else:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.freq[key] += 1
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    min_freq = min(self.freq.values())
                    lfu_keys = [
                        k for k, v in self.freq.items() if v == min_freq
                    ]
                    if len(lfu_keys) > 1:
                        lfu_key = next(
                            k for k in self.cache_data if k in lfu_keys
                        )
                    else:
                        lfu_key = lfu_keys[0]
                    del self.cache_data[lfu_key]
                    del self.freq[lfu_key]
                    print(f"DISCARD: {lfu_key}")

                self.cache_data[key] = item
                self.freq[key] = 1

    def get(self, key):
        """
        get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        else:
            self.freq[key] += 1
            return self.cache_data[key]
