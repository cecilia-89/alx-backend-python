#!/usr/bin/env python3
"""module: 1-concurrent coroutines"""
import asyncio

task_wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n, max_delay):
    """returns list of delays"""
    delay = await asyncio.gather(
      *(task_wait_random(max_delay) for _ in range(n)))
    return delay
