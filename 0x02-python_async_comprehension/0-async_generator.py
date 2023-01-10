#!/usr/bin/env python3
"""Module: 0-async generator"""
from typing import List
import asyncio
import random


async def async_generator() -> List[float]:
    """yields a random number for each iteration"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random()

