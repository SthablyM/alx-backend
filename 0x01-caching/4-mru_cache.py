#!/usr/bin/python3
"""
class  MRUCache that inherits from BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache that inherits from BaseCaching
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
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru_key = self.order.pop()
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")
        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None
        self.mru_order.remove(key)
        self.mru_order.append(key) 
        return self.cache_data[key]
