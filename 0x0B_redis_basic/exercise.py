#!/usr/bin/env python3
"""
Exercise file
"""
import redis
import uuid
from typing import Union, Callable
from functools import wraps


def call_history(method: Callable) -> Callable:
    """Decorator to store the history of inputs and outputs for a particular
    function
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapper function to store the history of inputs and outputs for a
        particular function"""
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        self._redis.rpush(input_key, str(args))

        output = method(self, *args, *kwargs)

        self._redis.rpush(output_key, output)

        return output
    return wrapper


def count_calls(method: Callable) -> Callable:
    """Decorator to count calls to a method.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function to count method calls."""
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


class Cache():
    """The class Cache
    """

    def __init__(self):
        """ Initialize the class
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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
