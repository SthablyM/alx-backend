#!/usr/bin/python3
"""
LFUCache
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    class LFUCache that inherits from BaseCaching and is a caching system
    """
    def __init__(self):
        """
        dictionary from the parent class
        """
        super().__init__()
        self.usage_frequency = {}
        self.access_order = {}
        self.current_order = 0

    def put(self, key, item):
        """
        assign to the dictionary self.cache_data
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            self.usage_frequency[key] += 1
            self.current_order += 1
            self.access_order[key] = self.current_order
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                least_freq = min(self.usage_frequency.values())
                lfu_keys = [
                        k for k,
                        v in self.usage_frequency.items()
                        if v == least_freq
                        ]
                lfu_key = min(lfu_keys, key=lambda k: self.access_order[k])
                del self.cache_data[lfu_key]
                del self.usage_frequency[lfu_key]
                del self.access_order[lfu_key]
                print(f"DISCARD: {lfu_key}")
            self.cache_data[key] = item
            self.usage_frequency[key] = 1
            self.current_order += 1
            self.access_order[key] = self.current_order

    def get(self, key):
        """
        return the value in self.cache_data linked to key
        """
        if key is None or key not in self.cache_data:
            return None
        self.usage_frequency[key] += 1
        self.current_order += 1
        self.access_order[key] = self.current_order
        return self.cache_data[key]
