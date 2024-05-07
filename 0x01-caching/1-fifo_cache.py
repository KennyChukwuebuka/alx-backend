#!/usr/bin/env python3
"""
    Write a class FIFOCache that inherits
    from BaseCaching and is a caching system
        Requirement
            use seld.cache_data dictionary
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data.pop(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                print("DISCARD: {}".format(list(self.cache_data.keys())[0]))
                self.cache_data.pop(list(self.cache_data.keys())[0])
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
