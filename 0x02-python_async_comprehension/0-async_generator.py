#!/usr/bin/env python3
"""
Async Generator
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:  # type: ignore
    """
    Generate random numbers from async generator
    """
    for _ in range(10):
        yield random.uniform(0, 10)
