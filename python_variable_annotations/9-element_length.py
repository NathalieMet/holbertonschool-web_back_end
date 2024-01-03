#!/usr/bin/env python3
"""def element_length"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns elements lengths"""
    return [(i, len(i)) for i in lst]
