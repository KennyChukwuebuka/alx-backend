#!/usr/bin/env python3
"""
    Create a class BasicCache that inherits from
    BaseCaching and is a caching system
        Requirement:
            use self.cache_data dictionary
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache defines:
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
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discard = list(self.cache_data.keys())[0]
                del self.cache_data[discard]
                print("DISCARD: {}".format(discard))

    def get(self, key):
        """ Get an item by key
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
