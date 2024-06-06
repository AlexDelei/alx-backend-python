#!/usr/bin/env python3
"""
string and int/float into a tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Combines the string and the integer into one tuple
    """
    return ((k, v**2))
