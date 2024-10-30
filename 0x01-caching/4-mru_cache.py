#!/usr/bin/python3
"""
MRUCache
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    class MRUCache that inherits from BaseCaching
    """
    def __init__(self):
        """
        assign to the dictionary
        """
        super().__init__()
        self.mru_order = []

    def put(self, key, item):
        """
        assign to the dictionary
        """

        if key is None or item is None:
            return
        if key in self.cache_data:
            self.mru_order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru_key = self.mru_order.pop()
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")
        self.cache_data[key] = item
        self.mru_order.append(key)

    def get(self, key):
        """
        Must return the value in self.cache_data linked to key.
        """
        if key is None or key not in self.cache_data:
            return None
        self.mru_order.remove(key)
        self.mru_order.append(key)
        return self.cache_data[key]
