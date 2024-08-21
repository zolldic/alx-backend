#!/usr/bin/env python3
""" 2. LIFO Caching  """
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache class implements a Last-In-First-Out caching system.

        Inherits from the BaseCaching class,
            providing a caching mechanism that discards
            the most recently added item when the cache reaches
            its maximum capacity.

        Methods:
            __init__(): Initializes the LIFOCache instance.
            put(key, item): Stores an item in the cache with the given key,
                following the LIFO policy.
            get(key): Retrieves an item from the cache using the given key.
    """
    def __init__(self):
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
        if key:
            self.cache_data[key] = item

        if len(self.cache_data) > self.MAX_ITEMS:
            last_key = list(self.cache_data)[-2]
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")

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
