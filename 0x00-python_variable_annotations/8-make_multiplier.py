#!/usr/bin/env python3
"""module: sum-list.py"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a a callback"""
    def callback(arg):
        """returns float multiplied by multiplier"""
        return arg * multiplier
    return callback
