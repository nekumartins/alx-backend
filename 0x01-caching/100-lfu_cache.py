#!/usr/bin/env python3
""" caching system
    """

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    Caching system that inherits from BaseCaching
    """

    def __init__(self) -> None:
        """constructor"""
        self.temp_list = {}
        super().__init__()

    def put(self, key, item):
        """
        Assign self.cache_data
        the item value for the key.
        """
        if not (key is None or item is None):
            self.cache_data[key] = item
            if len(self.cache_data.keys()) > self.MAX_ITEMS:
                pop = min(self.temp_list, key=self.temp_list.get)
                self.temp_list.pop(pop)
                self.cache_data.pop(pop)
                print(f"DISCARD: {pop}")
            if not (key in self.temp_list):
                self.temp_list[key] = 0
            else:
                self.temp_list[key] += 1

    def get(self, key):
        """
        Returns self.cache_data linked to key.
        """
        if (key is None) or not (key in self.cache_data):
            return None
        self.temp_list[key] += 1
        return self.cache_data.get(key)
