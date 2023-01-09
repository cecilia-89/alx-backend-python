#!/usr/bin/env python3
"""module: 1-concurrent coroutines"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    """returns list of delays"""
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return delays
