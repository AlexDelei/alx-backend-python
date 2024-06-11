#!/usr/bin/env python3
"""
Multiple coroutines with async
"""
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Using the as_completed module to list all the delays
    that were completed first.

    n  -- Number of times to spawn the function
    max_delay  -- Number of maximum delays
    """
    delayList = [wait_random(max_delay) for _ in range(n)]

    orderedList = asyncio.as_completed(delayList)
    delays = [await i for i in orderedList]
    return (delays)
