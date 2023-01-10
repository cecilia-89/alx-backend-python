#!/usr/bin/env python3
"""Module: 0-async generator"""
from typing import List
import asyncio
import random


async def async_generator() -> List[float]:
    """yields a random number for each iteration"""
    for _ in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)

async def print_yielded_values():
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

asyncio.run(print_yielded_values())
