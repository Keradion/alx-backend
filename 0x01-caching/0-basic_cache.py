#!/usr/bin/env python3
"""class BasicCache that inherits from BaseCaching and is a caching system."""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """caching system and it does not have a limit."""
    def put(self, key, item):
        """
           Must assign to the dictionary self.cache_data
           the item value for the key key.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Must return the value in self.cache_data linked to key."""
        return self.cache_data.get(key)
