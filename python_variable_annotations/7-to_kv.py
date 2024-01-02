#!/usr/bin/env python3
"""def to_kv"""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[float, int]) -> Tuple[str, float]:
    """takes a string k and an int OR float v as arguments and returns a
    tuple."""
    return (k, float(v) ** 2)
