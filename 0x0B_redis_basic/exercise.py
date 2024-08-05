#!/usr/bin/env python3
"""
Exercise file
"""
import redis
import uuid
from typing import Union, Callable


class Cache():
    """The class Cache
    """

    def __init__(self):
        """ Initialize the class
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Generate a random key (e.g. using uuid), store the input data in
        Redis sing the random key and return the key """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None):
        """ convert the data back to the desired format
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key):
        """ parametrize Cache.get with the correct conversion function for str
        """
        data = self.get(key, lambda x: x.decode('utf-8') if x else None)
        return data

    def get_int(self, key):
        """ parametrize Cache.get with the correct conversion function for int
        """
        data = self.get(key, lambda x: int(x) if x else None)
        return data

