#!/usr/bin/env python3
""" """
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
        BasicCache class implements a simple caching system.

        Methods:
            __init__(): Initializes the BasicCache instance.
            put(key, item): Stores an item in the cache with the given key.
            get(key): Retrieves an item from the cache using the given key.
    """
    def __init__(self):
        """
        Initializes the BasicCache instance.
        """
        super().__init__()

    def put(self, key, item):
        """Stores an item in the cache with the given key.

            Args:
                key (str): The key to use for storing the item.
                item (any): The item to store in the cache.
        """
        if key and item:
            self.cache_data[key] = item

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
