#!/usr/bin/env python3
"""
Creating tasks with async
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Using the as_completed module to list all the delays
    that were completed first.

    n  -- Number of times to spawn the function
    max_delay  -- Number of maximum delays
    """

    delayList = [task_wait_random(max_delay) for _ in range(n)]

    orderedList = asyncio.as_completed(delayList)
    delays = [await i for i in orderedList]
    return (delays)
