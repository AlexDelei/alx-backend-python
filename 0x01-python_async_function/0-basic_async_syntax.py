#!/usr/bin/env python3
"""
Async Basics
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    A simple example of async await
    """
    i = random.uniform(0, max_delay)  # max_value included and float value
    await asyncio.sleep(i)
    return (i)
