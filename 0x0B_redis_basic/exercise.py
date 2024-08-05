#!/usr/bin/env python3
"""
Exercise file
"""
import redis
import uuid


class Cache():
    """The class Cache
    """

    def __init__(self):
        """ Initialize the class
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: str | bytes | int | float) -> str:
        """ Generate a random key (e.g. using uuid), store the input data in
        Redis sing the random key and return the key """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
