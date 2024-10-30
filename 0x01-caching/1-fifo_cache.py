#!/usr/bin/python3
"""
class FIFOCache that inherits from BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache that inherits from BaseCaching
    """
    def __init__(self):
        """
        initializing class
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        assign to the dictionary
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.order.remove(key)
        self.cache_data[key] = item
        self.order.append(key)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            oldest_key = self.order.pop(0)
            del self.cache_data[oldest_key]
            print(f"DISCARD: {oldest_key}")

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key, None)
