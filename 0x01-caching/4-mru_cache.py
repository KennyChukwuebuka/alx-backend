#!/usr/bin/env python3
"""
    Write a class MRUCache that inherits from BaseCaching
"""

from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class that inherits from BaseCaching
    """

    def __init__(self):
        """
        Constructor to initialize the cache
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Add or update an item in the cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            del self.cache_data[key]

        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru_key, _ = self.cache_data.popitem(last=True)
            print("DISCARD:", mru_key)

        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache
        """
        if key is None or key not in self.cache_data:
            return None

        item = self.cache_data.pop(key)
        self.cache_data[key] = item
        return item
