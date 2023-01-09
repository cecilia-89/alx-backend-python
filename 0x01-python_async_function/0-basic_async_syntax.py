#!/usr/bin/env python3
"""module: 0-async"""
import asyncio
import random


async def wait_random(max_delay:int = 10) -> float:
    """returns a delay value"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
