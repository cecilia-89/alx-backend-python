#!/usr/bin/env python3
"""module: 1-concurrent coroutines"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delays: int) -> List[float]:
    """returns list of delayss"""
    delays = await asyncio.gather(*(wait_random(max_delays) for _ in range(n)))
    for i in range(1, len(delays)):
        key = delays[i]
        j = i - 1
        while j >= 0 and key < delays[j]:
            delays[j + 1] = delays[j]
            j -= 1
    delays[j + 1] = key

    return delays
