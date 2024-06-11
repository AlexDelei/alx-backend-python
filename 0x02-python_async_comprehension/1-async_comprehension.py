#!/usr/bin/env python3
"""
Async Comprehensions
"""
import random
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collect the random numbers using async comprehension
    """
    result = [rand async for rand in async_generator()]
    return result
