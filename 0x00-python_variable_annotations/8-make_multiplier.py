#!/usr/bin/env python3
"""
Multiplier function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a callable function that will multiplies
    the argument by the argument
    """
    def multiplier_func(val: float) -> float:
        """
        multiply floats
        """
        return (val * multiplier)

    return (multiplier_func)
