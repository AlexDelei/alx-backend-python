#!/usr/bin/env python3
"""
Multiple coroutines with async
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int):
    """
    n  -- Number of times to spawn the function
    max_delay  -- Number of maximum delays
    """
    delayList = []

    for _ in range(n):
        delayTime = await wait_random(max_delay)
        delayList.append(delayTime)

    async def orderList(lst: List[float]) -> List[float]:
        """
        Orders the list of unordered floats
        Using bubble sort algorithm
        """
        len_ = len(lst)

        for i in range(len_):
            for j in range(0, len_ - i - 1):
                if lst[j] > lst[j + 1]:
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]

        return (lst)

    orderedList = await orderList(delayList)

    return (orderedList)
