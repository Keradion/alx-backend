#!/usr/bin/env python3
""" class LIFOCache that inherits from BaseCaching and is a caching system."""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ caching system."""
    def put(self, key, item):
        """
           Must assign to the dictionary self.cache_data
           the item value for the key key.
        """
        if item is None or key is None:
            return
        
        self.cache_data[key] = item
        
        if len(self.cache_data)  > BaseCaching.MAX_ITEMS:
            value = self.cache_data.pop()
            print('DISCARD: {}'.format(self.c))

    def get(self, key):
        """Return item """
        return self.cache_data.get(key)
