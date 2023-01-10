#!/usr/bin/env python3
"""Module: 2-measure runtime"""
from asyncio import gather
from time import perf_counter


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """returns exextio time"""
    s = perf_counter()
    await gather(*(async_comprehension() for _ in range(4)))
    return perf_counter() - s
