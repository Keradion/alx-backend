#!/usr/bin/env python3
""" class LRUCache that inherits from BaseCaching and is a caching system."""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """Caching system based on LRU algorithm."""
    def get(self, key):
        """Return item """
        return self.cache_data.get(key)
