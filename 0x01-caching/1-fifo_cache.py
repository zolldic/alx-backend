#!/usr/bin/env python3
"""  1. FIFO caching """
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache class implements a First-In-First-Out caching system.

        Inherits from the BaseCaching class,
            providing a caching mechanism that discards
            the oldest item when the cache reaches its maximum capacity.

        Methods:
            __init__(): Initializes the FIFOCache instance.
            put(key, item): Stores an item in the cache with the given key,
                following the FIFO policy.
            get(key): Retrieves an item from the cache using the given key.
    """
    def __init__(self):
        """
        Initializes the FIFOCache instance.
        """
        super().__init__()

    def put(self, key, item):
        """
            Stores an item in the cache with the given key,
                following the FIFO policy.
            If the cache is full, the oldest item (first item added)
                is discarded before storing the new item.

            Args:
                key (str): The key to use for storing the item.
                item (any): The item to store in the cache.
        """
        if key and item:
            self.cache_data[key] = item

        if len(self.cache_data) > self.MAX_ITEMS:
            first_key = list(self.cache_data)[0]
            del self.cache_data[first_key]
            print(f"DISCARD: {first_key}")

    def get(self, key):
        """Retrieves an item from the cache using the given key.

            Args:
                key (str): The key to use for retrieving the item.

            Returns:
                The item stored in the cache with the given key,
                    or None if not found.
        """
        try:
            value = self.cache_data[key]
        except KeyError:
            return None
        return value
