#!/usr/bin/env python3
"""module: sum-list.py"""
from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns a list of tuple"""
    return [(i, len(i)) for i in lst]
