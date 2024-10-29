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
        # Based on LIFO algorithm Discard the First item
        # Determine If the cache is full first.
        if len(self.cache_data) == BaseCaching.MAX_ITEMS:
            # Remove first item
            first_item_key, item = self.cache_data.popitem()
            print('DISCARD: {}'.format(first_item_key))

        self.cache_data[key] = item

    def get(self, key):
        """Return item """
        return self.cache_data.get(key)
