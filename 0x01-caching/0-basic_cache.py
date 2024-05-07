#!/usr/bin/env python3
"""
    Create a class BasicCache that inherits from
    BaseCaching and is a caching system
        Requirement:
            use self.cache_data dictionary
"""

from base_caching import BaseCaching


class BaseCaching:
    def __init__(self):
        """
        Initializes the object with an empty cache_data dictionary.

        :param self: The object instance.
        :return: None
        """
        self.cache_data = {}

    def print_cache(self):
        """
        Print the current cache.

        This function prints the contents of the cache_data
        dictionary in a formatted way. It iterates over the
        keys of the dictionary and prints each key-value
        pair in the format "{key}: {value}".

        Parameters:
            self (BasicCache): The instance of the BasicCache class.

        Returns:
            None
        """
        print("Current cache:")
        for key in self.cache_data:
            print(f"{key}: {self.cache_data[key]}")


class BasicCache(BaseCaching):
    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key
        :param key: Key to retrieve the item from the cache
        :return: The item associated with the key if found, otherwise None
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
