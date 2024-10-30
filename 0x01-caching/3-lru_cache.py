#!/usr/bin/python3
"""
class  LRUCache that inherits from BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache that inherits from BaseCaching
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
            lru_key = self.order.pop(0)
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")
        self.cache_data[key] = item
        self.order.append(key)i

    def get(self, key):
        """return the value in self.cache_data"""
        if key is None or key not in self.cache_data:
            return None
        self.order.remove(key)
        self.order.append(key)
        
        return self.cache_data[key]