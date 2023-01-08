#!/usr/bin/env python3
"""module: sum-list.py"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int,  float]) -> Tuple[str, float]:
    """returns a tuple object"""
    return (k, v*v)
