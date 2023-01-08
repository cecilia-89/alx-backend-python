#!/usr/bin/env python3
"""module: sum-list.py"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns sum of a mixed list"""
    return float(sum(mxd_lst))
