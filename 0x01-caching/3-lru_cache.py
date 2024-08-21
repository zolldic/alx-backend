#!/usr/bin/env python3
""" 3. LRU Caching """
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """LRUCache that inherits from BaseCaching
        and implements the LRU algorithm."""
    def __init__(self):
        """Initializes the LRUCache instance."""
        self.order = []
        super().__init__()

    def put(self, key, item):
        """
            Inserts a key-value pair into the cache,
                following the LRU algorithm.

            Args:
                key (any): The key to store.
                item (any): The value to associate with the key.
        """
        if key in self.cache_data:
            self.order.remove(key)

        self.cache_data[key] = item
        self.order.append(key)

        if len(self.cache_data) > self.MAX_ITEMS:
            least = self.order.pop(0)
            del self.cache_data[least]
            print(f"DISCARD: {least}")

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
            self.order.remove(key)
            self.order.append(key)
        except KeyError:
            return None
        return value
