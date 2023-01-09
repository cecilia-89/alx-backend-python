#!/usr/bin/env python3
"""module: 2-measure runtime"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n, max_delay):
    """returns time completion of a async function"""
    s = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    return ((time.perf_counter() - s) / float(n))
